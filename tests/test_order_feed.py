from conftest import *
import allure
from fake_data import FakerMethods
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:
    @allure.title('Проверка открытия окна с деталями при клике на заказ в ленте')
    def test_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        with allure.step('Кликнуть по кнопке Лента заказов'):
            main_page.click_on_order_feed_button()
            order_feed_page.check_text_in_order_feed_page()
        with allure.step('Кликнуть по карточке'):
            order_feed_page.click_on_card_in_feed()
        with allure.step('Проверка отображения модального окна'):
            assert order_feed_page.check_modal_window_is_visible() == 'Cостав'

    @allure.title('Проверка отображения заказов пользователя'
                  ' из истории заказов на странице ленты заказов')
    def test_orders_displayed_from_history_on_feed(self, driver):
        with allure.step('Создать пользователя'):
            user_data = FakerMethods.create_user()
            main_page = MainPage(driver)
            account_page = PersonalAccountPage(driver)
        with allure.step('Авторизация и добавление ингредиента'):
            main_page.click_omy_personal_account_in_header()
            account_page.login(user_data['email'], user_data['password'])
            main_page.click_on_constructor_button_in_header()
            main_page.add_ingredient_to_order()
            main_page.click_on_order_button()
            main_page.click_on_close_ingredient_card()
            account_page.click_on_personal_account_header()
            account_page.wait_for_display_description_text()
            account_page.click_order_history_button()
            account_page.wait_for_card_in_history()
        with allure.step('Получение идентификатора заказа'):
            card_id = account_page.get_id_of_order_card()
            main_page.click_on_order_feed_button()
        with allure.step('Проверка наличия в ленте'):
            assert card_id in main_page.get_orders_list_from_main_page()
        with allure.step('Удаление пользователя'):
            FakerMethods.delete_user(access_token=user_data['accessToken'])

    @allure.title('Проверка увеличения счетчика Выполнено за всё время при создании заказа')
    def test_increase_done_counter_on_create_order(self, driver):
        with allure.step('Создание пользователя'):
            user_data = FakerMethods.create_user()
            main_page = MainPage(driver)
            account_page = PersonalAccountPage(driver)
        with allure.step('Вход в аккаунт пользователя'):
            main_page.click_omy_personal_account_in_header()
            account_page.login(user_data['email'], user_data['password'])
        with allure.step('Переход в ленту заказов'):
            main_page.click_on_order_feed_button()
            order_feed_page = OrderFeedPage(driver)
        with allure.step('Считаем количество заказов'):
            count_of_orders_before = order_feed_page.get_count_of_orders()
        with allure.step('Создаем заказ'):
            main_page.click_on_constructor_button_in_header()
            main_page.add_ingredient_to_order()
            main_page.click_on_order_button()
            main_page.click_on_close_ingredient_card()
        with allure.step('Проверка количества заказов'):
            main_page.click_on_order_feed_button()
            count_of_orders_after = order_feed_page.get_count_of_orders()
            assert count_of_orders_after > count_of_orders_before
        with allure.step('Удаление пользователя'):
            FakerMethods.delete_user(access_token=user_data['accessToken'])

    @allure.title('Проверка увеличения счетчика Выполнено за сегодня при создании заказа')
    def test_increase_done_daily_counter_on_create_order(self, driver):
        with allure.step('Создание пользователя'):
            user_data = FakerMethods.create_user()
            main_page = MainPage(driver)
            account_page = PersonalAccountPage(driver)
        with allure.step('Вход в аккаунт пользователя'):
            main_page.click_omy_personal_account_in_header()
            account_page.login(user_data['email'], user_data['password'])
        with allure.step('Переход в личный кабинет'):
            main_page.click_on_order_feed_button()
            order_feed_page = OrderFeedPage(driver)
        with allure.step('Считаем количество заказов'):
            count_of_orders_before = order_feed_page.get_count_of_orders_per_day()
        with allure.step('Создаем заказ'):
            main_page.click_on_constructor_button_in_header()
            main_page.add_ingredient_to_order()
            main_page.click_on_order_button()
            main_page.click_on_close_ingredient_card()
        with allure.step('Проверка количества заказов'):
            main_page.click_on_order_feed_button()
            count_of_orders_after = order_feed_page.get_count_of_orders_per_day()
            assert count_of_orders_after > count_of_orders_before
        with allure.step('Удаление пользователя'):
            FakerMethods.delete_user(access_token=user_data['accessToken'])

    @allure.title("После оформления заказа, его номер появляется в разделе 'В работе'")
    def test_order_number_displayed_in_work_section(self, driver):
        with allure.step('Создание пользователя'):
            user_data = FakerMethods.create_user()
            main_page = MainPage(driver)
            order_feed_page = OrderFeedPage(driver)
            account_page = PersonalAccountPage(driver)
        with allure.step('Вход в аккаунт пользователя'):
            main_page.click_omy_personal_account_in_header()
            account_page.login(user_data['email'], user_data['password'])
        with allure.step('Переход в личный кабинет'):
            main_page.click_on_order_feed_button()
        with allure.step('Создаем заказ'):
            main_page.click_on_constructor_button_in_header()
            main_page.add_ingredient_to_order()
            main_page.click_on_order_button()
            with allure.step('Получить номер заказа'):
                order_id = main_page.get_number_of_order_in_modal_confirmation()
                main_page.click_on_close_ingredient_card()
                main_page.click_on_order_feed_button()
            with allure.step('Проверка наличия в разделе "В работе"'):
                assert order_feed_page.get_number_order_in_feed_progress() == "0" + order_id
            with allure.step('Удаление пользователя'):
                FakerMethods.delete_user(access_token=user_data['accessToken'])








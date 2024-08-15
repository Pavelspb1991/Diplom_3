from conftest import *
import allure
from fake_data import FakerMethods
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestMainFunctionality:
    @allure.title('Проверка перехода по клику на  Конструктор')
    def test_main_page(self, driver):
        main_page = MainPage(driver)
        with allure.step('Кликнуть по кнопке Конструктор'):
            main_page.click_on_personal_account_button()
            main_page.click_on_constructor_button_in_header()
            main_page.wait_for_constructor_text()
        with allure.step('Проверка отображения текста Конструктор'):
            assert main_page.check_displaying_constructor_text()

    @allure.title('Проверка перехода по клику на Ленту заказов')
    def test_order_feed_history(self, driver):
        main_page = MainPage(driver)
        with allure.step('Кликнуть по кнопке Лента заказов'):
            order_feed_page = OrderFeedPage(driver)
            main_page.click_on_order_feed_button()
        with allure.step('Проверка отображения текста Лента заказов'):
            assert order_feed_page.check_text_in_order_feed_page() == 'Лента заказов'

    @allure.title('Проверка открытия окна с деталями при клике на ингредиент в ленте заказов')
    def test_modal_window_is_displayed_after_ingredient_selection(self, driver):
        main_page = MainPage(driver)
        with allure.step('Кликнуть по ингредиенту в ленте заказов'):
            main_page.wait_for_constructor_text()
            main_page.click_on_product_card()
            main_page.wait_for_ingredient_card()
        with allure.step('Проверка отображения окна с деталями'):
            assert main_page.check_displaying_ingredient_card_modal()

    @allure.title('Проверка закрытия окна с деталями при клике на крестик')
    def test_modal_window_is_closed_after_closing(self, driver):
        main_page = MainPage(driver)
        with allure.step('Кликнуть по ингредиенту в ленте заказов'):
            main_page.wait_for_constructor_text()
            main_page.click_on_product_card()
            main_page.wait_for_ingredient_card()
        with allure.step('Кликнуть по крестику'):
            main_page.click_on_close_ingredient_card()
        with allure.step('Проверка закрытия окна с деталями'):
            assert main_page.check_ingredient_card_modal_close()

    @allure.title('Проверка увеличения счетчика при добавлении ингредиента в заказ')
    def test_counter_increase_success(self, driver):
        main_page = MainPage(driver)
        with allure.step('Добавить ингредиент в заказ'):
            main_page.add_ingredient_to_order()
        with allure.step('Проверка количества добавленных ингредиентов'):
            assert main_page.check_count_of_ingredients() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_user_can_order(self, driver):
        with allure.step('Создать пользователя'):
            user_data = FakerMethods.create_user()
            main_page = MainPage(driver)
        with allure.step('Залогиниться'):
            main_page.click_omy_personal_account_in_header()
            main_page.login(user_data['email'], user_data['password'])
        with allure.step('Добавить ингредиент в заказ'):
            main_page.wait_for_constructor_text()
            main_page.add_ingredient_to_order()
            main_page.click_on_order_button()
        with allure.step('Проверка создания заказа'):
            assert main_page.check_order_modal_success()
        with allure.step('Удалить пользователя'):
            FakerMethods.delete_user(access_token=user_data['accessToken'])










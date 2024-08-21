from fake_data import *
from conftest import *
import allure
from locators.personal_account_locators import PersonalAccountLocators
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    class TestPersonalAccount:
        @allure.title('Проверка перехода в личный кабинет при клике на кнопку "Личный кабинет"')
        def test_personal_account(self, driver):
            with allure.step('Создание пользователя'):
                user_data = FakerMethods.create_user()
                main_page = MainPage(driver)
                account_page = PersonalAccountPage(driver)
            with allure.step('Авторизация'):
                main_page.click_omy_personal_account_in_header()
                account_page.login(user_data['email'], user_data['password'])
            account_page.click_on_personal_account_header()
            account_page.wait_auth_personal_account()
            with allure.step('Проверка отображения личного кабинета'):
                assert account_page.check_auth_personal_account()
            with allure.step('Удаление пользователя'):
                FakerMethods.delete_user(access_token=user_data['accessToken'])

    @allure.title('Проверка перехода в раздел История заказов по клику на кнопку "История заказов"')
    def test_order_history(self, driver):
        with allure.step('Создание пользователя'):
            user_data = FakerMethods.create_user()
            order_payload = FakerMethods.burger
            FakerMethods.create_order(order_payload, access_token=user_data['accessToken'])
            main_page = MainPage(driver)
            account_page = PersonalAccountPage(driver)
        with allure.step('Авторизация'):
            main_page.click_omy_personal_account_in_header()
            account_page.login(user_data['email'], user_data['password'])
            account_page.click_on_personal_account_header()
            account_page.wait_for_display_description_text()
        with allure.step('Клик по кнопке "История заказов"'):
            account_page.click_order_history_button()
            account_page.wait_for_card_in_history()
        with allure.step('Проверка загрузки карточки в "Истории заказов"'):
            assert 'бургер' in account_page.get_text(PersonalAccountLocators.order_history_card)
        with allure.step('Удаление пользователя'):
            FakerMethods.delete_user(access_token=user_data['accessToken'])

    @allure.title('Проверка выхода по клику на кнопку "Выход"')
    def test_personal_account_exit(self, driver):
        with allure.step('Создание пользователя'):
            user_data = FakerMethods.create_user()
            main_page = MainPage(driver)
            account_page = PersonalAccountPage(driver)
        with allure.step('Авторизация'):
            main_page.click_omy_personal_account_in_header()
            account_page.login(user_data['email'], user_data['password'])
            main_page.click_omy_personal_account_in_header()
        with allure.step('Клик по кнопке "Выход"'):
            account_page.exit_click_wait()
            account_page.click_exit_button()
            account_page.wait_for_displaying_of_input_button_in_account()
        with allure.step('Проверка перехода на страницу логина'):
            assert account_page.current_url() == f'{TestUrls.USER_LOGOUT}'
        with allure.step('Удаление пользователя'):
            FakerMethods.delete_user(access_token=user_data['accessToken'])

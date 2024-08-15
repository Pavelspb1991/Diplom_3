from fake_data import *
from conftest import *
import allure
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage


class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        with allure.step('Нажатие кнопки войти в аккаунт'):
            main_page.click_on_personal_account_button()
            recovery_page = RecoveryPage(driver)
        with allure.step('Нажатие кнопки восстановить пароль'):
            recovery_page.click_on_personal_account()
            recovery_page.wait_input_email_is_visible()
        with allure.step('Проверка перехода на страницу восстановления пароля'):
            assert recovery_page.check_input_email_is_visible()

    @allure.title('Проверка перехода на страницу восстановления пароля и нажатия кнопки восстановить пароль')
    def test_enter_email(self, driver):
        with allure.step('Нажатие кнопки войти'):
            main_page = MainPage(driver)
            main_page.click_on_personal_account_button()
            recovery_page = RecoveryPage(driver)
            recovery_page.click_on_personal_account()
        with allure.step('Ввод email'):
            recovery_page.input_recovery_email(fake.free_email())
            recovery_page.click_on_recovery_button()
        with allure.step('Проверка перехода на страницу восстановления пароля'):
            assert recovery_page.check_input_password_is_visible()

    @allure.title('Проверка отображения пароля при'
                  ' нажатии на кнопку показать пароль(password eye)')
    def test_show_password(self, driver):
        main_page = MainPage(driver)
        with allure.step('Нажатие кнопки войти'):
            main_page.click_on_personal_account_button()
            recovery_page = RecoveryPage(driver)
        with allure.step('Ввести email'):
            recovery_page.click_on_personal_account()
            recovery_page.input_recovery_email(fake.email())
            recovery_page.click_on_recovery_button()
        with allure.step('Ввод пароля'):
            recovery_page.input_recovery_password(fake.password())
            recovery_page.click_on_eye_icon()
        with allure.step('Проверка отображения пароля'):
            assert recovery_page.check_password_values_is_visible()

    @allure.title('Проверка скрытия пароля при нажатии на кнопку скрыть пароль(password eye)')
    def test_show_password(self, driver):
        main_page = MainPage(driver)
        with allure.step('Нажатие кнопки войти'):
            main_page.click_on_personal_account_button()
            recovery_page = RecoveryPage(driver)
            recovery_page.click_on_personal_account()
        with allure.step('Ввести email'):
            recovery_page.input_recovery_email(fake.email())
            recovery_page.click_on_recovery_button()
        with allure.step('Ввод пароля'):
            recovery_page.input_recovery_password(fake.password())
        with allure.step('Нажатие на кнопку скрыть пароль'):
            recovery_page.click_on_eye_icon()
            recovery_page.click_on_eye_icon()
        with allure.step('Проверка скрытия пароля'):
            assert recovery_page.check_password_values_is_invisible()









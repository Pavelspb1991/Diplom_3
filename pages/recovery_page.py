from pages.base_page import BasePage
import allure
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators


class RecoveryPage(BasePage):

    @allure.step('Кликнуть по кнопке восстановить пароль')
    def click_on_personal_account(self):
        self.wait_for_element_visible(RecoveryPasswordPageLocators.button_recovery_password)
        self.click_on_element(RecoveryPasswordPageLocators.button_recovery_password)

    @allure.step('Ввести email в поле ввода')
    def input_email(self, email):
        self.wait_for_element_visible(RecoveryPasswordPageLocators.input_email)
        self.send_keys_input(RecoveryPasswordPageLocators.input_email, email)

    @allure.step('Кликнуть по кнопке восстановить пароль')
    def click_on_recovery_button(self):
        self.wait_for_element_visible(RecoveryPasswordPageLocators.button_recovery)
        self.click_on_element(RecoveryPasswordPageLocators.button_recovery)

    @allure.step('Проверка видимости поле ввода восстановления email')
    def check_input_email_is_visible(self):
        return self.check_element_is_visible(RecoveryPasswordPageLocators.input_recovery_email)

    @allure.step('Проверка ожидания поле ввода восстановления email')
    def wait_for_element_clickable(self):
        self.wait_for_element_visible(RecoveryPasswordPageLocators.input_recovery_email)

    @allure.step('Ввод email в поле восстановления')
    def input_recovery_email(self, email):
        self.wait_for_element_visible(RecoveryPasswordPageLocators.input_recovery_email)
        self.send_keys_input(RecoveryPasswordPageLocators.input_recovery_email, email)

    @allure.step('Проверка видимости поле ввода пароля после восстановления почты')
    def check_input_password_is_visible(self):
        self.wait_for_element_visible(RecoveryPasswordPageLocators.input_password)
        return self.check_element_is_visible(RecoveryPasswordPageLocators.input_password)

    @allure.step('Кликнуть по иконке password eye')
    def click_on_eye_icon(self):
        self.wait_for_element_visible(RecoveryPasswordPageLocators.icon_hide_password)
        self.click_on_element(RecoveryPasswordPageLocators.icon_hide_password)

    @allure.step('Проверка состояния поля ввода - пароль виден')
    def check_password_values_is_visible(self):
        return self.check_element_is_visible(RecoveryPasswordPageLocators.password_visible)

    @allure.step('Проверка состояния поля ввода - пароль скрыт')
    def check_password_values_is_invisible(self):
        return self.check_element_is_visible(RecoveryPasswordPageLocators.password_invisible)

    @allure.step('Ввод пароля в поле восстановления пароля')
    def input_recovery_password(self, password):
        self.wait_for_element_visible(RecoveryPasswordPageLocators.input_password)
        self.send_keys_input(RecoveryPasswordPageLocators.input_password, password)








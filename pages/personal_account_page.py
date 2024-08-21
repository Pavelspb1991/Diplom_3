import allure
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.base_page_locators import BasePageLocators


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввести почту и пароль')
    def login(self, email, password):
        self.wait_for_element_visible(PersonalAccountLocators.input_email)
        self.send_keys_input(PersonalAccountLocators.input_email, email)
        self.send_keys_input(PersonalAccountLocators.input_password, password)
        self.click_on_element(PersonalAccountLocators.login_button)

    @allure.step('Проверка отображения раздела "Личный кабинет"')
    def wait_auth_personal_account(self):
        self.wait_for_element_visible(PersonalAccountLocators.personal_account_info)

    @allure.step('Проверка  раздела "Личный кабинет"')
    def check_auth_personal_account(self):
        return self.wait_for_element_visible(PersonalAccountLocators.personal_account_info)

    @allure.step('Подождать загрузку текста описания раздела')
    def wait_for_display_description_text(self):
        self.wait_for_element_visible(PersonalAccountLocators.description_text_personal_account)

    @allure.step('Кликнуть по кнопке "История заказов"')
    def click_order_history_button(self):
        self.click_on_element(PersonalAccountLocators.history_orders_button)

    @allure.step('Проверка загрузки карточки  в "Истории заказов"')
    def check_card_in_history(self):
        self.check_element_is_visible(PersonalAccountLocators.order_history_card)

    @allure.step('Подождать загрузку карточки в "Истории заказов"')
    def wait_for_card_in_history(self):
        self.wait_for_element_visible(PersonalAccountLocators.order_history_card)

    @allure.step('Получить текст карточки заказа')
    def get_text_of_order_card_title(self):
        return self.get_text(PersonalAccountLocators.order_history_card)

    @allure.step('Кликнуть по кнопке "Выход"')
    def click_exit_button(self):
        self.click_on_element_force(PersonalAccountLocators.exit_button)

    @allure.step('Проверка отображения кнопки "Войти"')
    def check_displaying_of_login_button(self):
        return self.check_element_is_visible(PersonalAccountLocators.login_button)

    @allure.title('Ождиание отображения кнопки  Войти')
    def wait_for_displaying_of_input_button_in_account(self):
        self.wait_for_element_visible(PersonalAccountLocators.login_button)

    @allure.step('Ожидание кнопки "Выход" с проверкой выхода')
    def exit_click_wait(self):
        self.wait_for_element_clickable(PersonalAccountLocators.exit_button)

    @allure.step('Нажатие на кнопку Личный кабинет')
    def click_on_personal_account_header(self):
        self.wait_for_element_visible(BasePageLocators.personal_account_button)
        self.wait_for_element_clickable(BasePageLocators.personal_account_button)
        self.click_on_element(BasePageLocators.personal_account_button)

    @allure.step('Получить номер заказа из карточки заказа')
    def get_id_of_order_card(self):
        return self.get_text(PersonalAccountLocators.order_id_in_history)
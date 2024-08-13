from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage
import allure
from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке войти в аккаунт')
    def click_on_personal_account_button(self):
        self.wait_for_element_visible(BasePageLocators.input_button)
        self.click_on_element(BasePageLocators.input_button)

    @allure.step('Кликнуть по кнопке войти в аккаунт')
    def click_on_personal_account_force(self):
        self.wait_for_element_visible(BasePageLocators.input_button)
        self.click_force()

    @allure.step('Кликнуть по кнопке Личный аккаунт')
    def click_omy_personal_account_in_header(self):
        self.wait_for_element_clickable(BasePageLocators.personal_account_button)
        self.click_on_element(BasePageLocators.personal_account_button)

    def set_get_access_token(self, access_token):
        self.driver.execute_script(f"localStorage.setItem('accessToken', '{access_token}');")
        return self.driver.execute_script("return localStorage.getItem('accessToken')")

    @allure.step('Кликнуть по кнопке Конструктор')
    def click_on_constructor_button_in_header(self):
        self.wait_for_element_clickable(BasePageLocators.constructor_button)
        self.click_on_element(BasePageLocators.constructor_button)

    @allure.step('Ожидание загрузки описания Конструктора')
    def wait_for_constructor_text(self):
        self.wait_for_element_visible(BasePageLocators.constructor_text)

    @allure.step('Проверка отображения описания Конструктора')
    def check_displaying_constructor_text(self):
        return self.get_text(BasePageLocators.constructor_text)

    @allure.step('Кликнуть по кнопке Лента заказов')
    def click_on_order_feed_button(self):
        self.wait_for_element_clickable(BasePageLocators.order_feed_button_header)
        self.click_on_element(BasePageLocators.order_feed_button_header)

    @allure.step('Кликнуть по карточке товара')
    def click_on_product_card(self):
        self.wait_for_element_clickable(BasePageLocators.ingredient_card)
        self.click_on_element(BasePageLocators.ingredient_card)

    @allure.step('Ожидание загрузки карточки товара')
    def wait_for_ingredient_card(self):
        self.wait_for_element_visible(BasePageLocators.ingredient_card_modal)

    @allure.step('Проверка отображения карточки товара')
    def check_displaying_ingredient_card_modal(self):
        return self.check_element_is_visible(BasePageLocators.ingredient_card_modal)

    @allure.step('Кликнуть по кнопке закрыть карточку')
    def click_on_close_ingredient_card(self):
        self.wait_for_element_clickable(BasePageLocators.modal_close_button)
        self.click_on_element(BasePageLocators.modal_close_button)

    @allure.step('Проверка закрытия  карточки товара')
    def check_ingredient_card_modal_close(self):
        if not self.check_element_is_clickable(BasePageLocators.modal_close_button):
            return True

    @allure.step('Добавить интгридиенты в заказ')
    def add_ingredient_to_order(self):
        drag = self.find_element_with_wait(BasePageLocators.ingredient_card)
        drop = self.find_element_with_wait(BasePageLocators.order_list)
        self.drag_and_drop(drag, drop)

    @allure.step('Проверка количества ингредиентов в заказе')
    def check_count_of_ingredients(self):
        self.wait_for_element_visible(BasePageLocators.count_of_buns)
        return self.get_text(BasePageLocators.count_of_buns)

    @allure.step('Ввести почту и пароль')
    def login(self, email, password):
        self.wait_for_element_visible(PersonalAccountLocators.input_email)
        self.send_keys_input(PersonalAccountLocators.input_email, email)
        self.send_keys_input(PersonalAccountLocators.input_password, password)
        self.click_on_element(PersonalAccountLocators.login_button)

    @allure.step('Кликнуть по кнопке оформить заказ')
    def click_on_order_button(self):
        self.wait_for_element_clickable(BasePageLocators.button_get_order)
        self.click_on_element(BasePageLocators.button_get_order)

    @allure.step('Проверка создания заказа')
    def check_order_modal_success(self):
        self.wait_for_element_visible(BasePageLocators.order_modal)
        return self.check_element_is_visible(BasePageLocators.order_modal)

    @allure.step("Получение списка заказов")
    def get_orders_list_from_main_page(self):
        return self.find_element_with_wait(BasePageLocators.all_orders_list).text

    @allure.step('Получить номер заказа из модального окна')
    def get_number_of_order_in_modal_confirmation(self):
        self.wait_for_element_correct_value(BasePageLocators.order_number_in_modal, '9999')
        return self.get_text(BasePageLocators.order_number_in_modal)


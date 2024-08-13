import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    @allure.title('Проверка отображения  элемента h1 раздела "Лента заказов"')
    def check_text_in_order_feed_page(self):
        self.wait_for_element_visible(OrderFeedPageLocators.order_feed_text_h1)
        return self.get_text(OrderFeedPageLocators.order_feed_text_h1)

    @allure.step('Клик по заказу в ленте')
    def click_on_card_in_feed(self):
        self.wait_for_element_visible(OrderFeedPageLocators.order_card_in_feed)
        self.click_on_element(OrderFeedPageLocators.order_card_in_feed)

    def check_modal_window_is_visible(self):
        self.wait_for_element_visible(OrderFeedPageLocators.order_modal_window_description)
        return self.get_text(OrderFeedPageLocators.order_modal_window_description)

    @allure.step('Количество заказов за все время')
    def get_count_of_orders(self):
        self.find_element_with_wait(OrderFeedPageLocators.count_of_orders)
        return self.get_text(OrderFeedPageLocators.count_of_orders)

    @allure.step('Количество заказов за сегодня')
    def get_count_of_orders_per_day(self):
        self.find_element_with_wait(OrderFeedPageLocators.count_of_orders_per_day)
        return self.get_text(OrderFeedPageLocators.count_of_orders_per_day)

    @allure.step('Номер заказа в ленте заказов')
    def get_number_order_in_feed_progress(self):
        self.find_element_with_wait(OrderFeedPageLocators.number_order_feed_page_progress_list)
        return self.get_text(OrderFeedPageLocators.number_order_feed_page_progress_list)



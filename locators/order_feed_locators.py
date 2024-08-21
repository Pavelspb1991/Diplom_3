from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    # Текст в разделе "Лента заказов"
    order_feed_text_h1 = (By.XPATH, '//h1[text() = "Лента заказов"]')
    # Карточка заказа в ленте
    order_card_in_feed = (By.XPATH, './/li[contains(@class, "OrderHistory_listItem")][1]')
    # Поле с описанием заказа
    order_modal_window_description = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                                '//div[contains(@class,"Modal_orderBox")]//p[3]')
    # Все заказы
    all_orders_list = (By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']")
    # Количество выполненных заказов
    count_of_orders = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    # Количество выполненных заказов за сегодня
    count_of_orders_per_day = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    # Номер заказа в ленте
    number_order_feed_page_progress_list = (
        By.XPATH, '//ul[contains(@class,"OrderFeed_orderListReady")]/li[contains(@class, '
                  '"text_type_digits-default")]')

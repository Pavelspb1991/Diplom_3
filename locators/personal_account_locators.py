from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    # Локатор описания личного кабинета
    description_text_personal_account = (By.CSS_SELECTOR, ".text.text_type_main-default")
    # Поле ввода почты
    input_email = (By.XPATH, "//input[@type='text' and @name='name']")
    # Поле ввода пароля
    input_password = (By.XPATH, "//input[@type='password']")
    # Кнопка История заказов
    history_orders_button = (By.XPATH, '//a[@href = "/account/order-history"]')
    # Карточки в истории заказов
    order_history_card = (By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]")
    # Кнопка выход
    exit_button = (By.XPATH, './/button[contains(text(), "Выход")]')
    # Кнопка "Войти"
    login_button = (By.XPATH, ".//button[text() = 'Войти']")
    # Информация о личном кабинете
    personal_account_info = (By.XPATH, "//p[contains(@class, 'Account_text')]")
    # Идентификатор заказа в истории
    order_id_in_history = (By.XPATH, ".//p[@class='text text_type_digits-default']")



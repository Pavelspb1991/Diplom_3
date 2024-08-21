from selenium.webdriver.common.by import By


class BasePageLocators:
    # Кнопка войти
    input_button = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    # Кнопка Личный Кабинет
    personal_account_button = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка Конструктор
    constructor_button = (By.XPATH, '//p[text() = "Конструктор"]')
    # Текст в конструкторе
    constructor_text = (By.XPATH, '//h1[text() = "Соберите бургер"]')
    # Кнопка Лента заказов в хедере
    order_feed_button_header = (By.XPATH, "//a[@href='/feed']")
    # Карточка ингредиента
    ingredient_card = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')
    # Кнопка с ингредиентами
    ingredient_card_modal = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    # Кнопка закрытия модального окна
    modal_close_button = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]')
    # Список заказов
    order_list = (By.XPATH, '(//section[contains(@class, "BurgerConstructor_basket")]//li)[1]')
    # Количество булочек
    count_of_buns = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]'
                               '//p[@class="counter_counter__num__3nue1"][1]')
    # Кнопка "Оформить заказ"
    button_get_order = (By.XPATH, './/button[text()="Оформить заказ"]')
    # Модальное окно
    order_modal = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains(@class, "Modal_modal__container")]')
    # Список всех заказов
    all_orders_list = (By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']")
    # Номер заказа в модальном окне
    order_number_in_modal = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')


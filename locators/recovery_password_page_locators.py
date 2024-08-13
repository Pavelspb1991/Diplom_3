from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:
    # Поле ввода email
    input_email = (By.XPATH, "//input[@type='text' and @name='name']")
    # Поле ввода пароля
    input_password = (By.XPATH, "//input[@type='password']")
    # Локатор для кнопки "Восстановить пароль"
    button_recovery_password = (By.XPATH, '//a[text() = "Восстановить пароль"]')
    # Локатор для иконки "Скрыть пароль"
    icon_hide_password = (By.CSS_SELECTOR, ".input__icon.input__icon-action > svg")
    # Локатор для состояния "Пароль виден"
    password_visible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                  '"input_status_active")]')
    # Локатор для состояния "Пароль скрыт"
    password_invisible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                    '"input_type_password")]')
    # Локатор для кнопки "Восстановить"
    button_recovery = (By.XPATH, '//button[text() = "Восстановить"]')

    # Локатор для поля ввода email восстановления пароля
    input_recovery_email = (By.CSS_SELECTOR, "input.text.input__textfield[name='name']")

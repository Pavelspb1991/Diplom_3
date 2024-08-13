import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание появления элемента')
    def wait_for_element_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Наведение курсора на элемент')
    def hover(self, locator):
        hover = ActionChains(self.driver).move_to_element(locator)
        hover.perform()

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        element = self.check_element_is_clickable(locator)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Кликнуть с помощью JS')
    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element_with_wait())

    @allure.step('Ожидание кликабельности элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    @allure.step('Проверка видимости элемента')
    def check_element_is_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Ввод значение в поле ввода')
    def send_keys_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Найти элемент на странице')
    def find_element_with_wait(self, locator):
        self.wait_for_element_visible(locator)
        return self.driver.find_element(*locator)

    @allure.step('Подождать, пока элемент закроется')
    def wait_for_closing_of_element(self, locator):
        WebDriverWait(self.driver, 15).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        self.wait_for_element_visible(locator)
        return self.driver.find_element(*locator).text

    def current_url(self):
        return self.driver.current_url

    @allure.step('Кликнуть на элемент')
    def click_on_element_force(self, locator):
        element = self.check_element_is_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, drag, drop):
        ActionChains(self.driver).drag_and_drop(drag, drop).pause(3).perform()

    @allure.step('Ожидание смены цифр в элементе')
    def wait_for_element_correct_value(self, locator, value):
        return WebDriverWait(self.driver, 10).until_not(EC.
                                                        text_to_be_present_in_element(locator, value))





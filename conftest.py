import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from test_urls import TestUrls
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1700,1000")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        firefox_options = Options()
        firefox_options.add_argument("--width=1700")
        firefox_options.add_argument("--height=1000")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError("Ошибка драйвера")
    driver.get(TestUrls.BASE_URL)
    yield driver
    driver.quit()


# Для запусков без ошибок
@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    import time
    time.sleep(1)

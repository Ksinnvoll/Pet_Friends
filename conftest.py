import pytest
from selenium import webdriver      #подключили библиотеку
from selenium.webdriver.chrome.service import Service

@pytest.fixture(autouse=True)
def driver():
    driver = Service('Selenium/driver/')
    driver = webdriver.Chrome(service=driver)
    driver.maximize_window()  # размер окна браузера по рамеру экрана
    return driver

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.set_headless(True)       #headledd режим Хрома
    return chrome_options

@pytest.fixture
def web_browser(request, driver):
    browser = driver
    browser.set_window_size(1400, 1000)

    # Вернуть объект браузера
    yield browser

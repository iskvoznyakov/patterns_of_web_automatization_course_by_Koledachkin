from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # TODO Добавить общие для всех страниц локаторы

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    # TODO Добавить общие для всех страниц методы

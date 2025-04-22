from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):
    # TODO Добавить общие для всех страниц локаторы

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self):
        with allure.step(f"Open page:{self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)

    def find_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator), f"There's no element: {locator}")
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

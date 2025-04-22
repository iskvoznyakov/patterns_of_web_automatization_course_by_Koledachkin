import allure

from base.base_page import BasePage


class LoginPage(BasePage):
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/login"

    _USERNAME_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _LOGIN_BUTTON = "//input[@value='Login']"
    _ERROR_MESSAGE = "//div[contains(@class, 'alert-danger')]"

    @allure.step("Enter login")
    def enter_login(self, username):
        self.enter_text(self._USERNAME_FIELD, username)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.enter_text(self._PASSWORD_FIELD, password)

    @allure.step("Click on a login button")
    def click_login_button(self):
        allure.attach(body=self.driver.get_screenshot_as_png(), name="Filled form before login",
                      attachment_type=allure.attachment_type.PNG)
        self.click(self._LOGIN_BUTTON)

    @allure.step("Check if the error message is visibile")
    def is_error_message_visible(self):
        return self.find_element(self._ERROR_MESSAGE).is_displayed()

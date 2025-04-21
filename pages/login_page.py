from base.base_page import BasePage


class LoginPage(BasePage):
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/login"

    _USERNAME_FIELD = ("xpath", "//input[@name='username']")
    _PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    _LOGIN_BUTTON = ("xpath", "//input[@value='Login']")
    _ERROR_MESSAGE = ("xpath", "//div[contains(@class, 'alert-danger')]")

    def enter_login(self, username):
        self.enter_text(self._USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(self._PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(self._LOGIN_BUTTON)

    def is_error_message_visible(self):
        return self.find_element(self._ERROR_MESSAGE).is_displayed()
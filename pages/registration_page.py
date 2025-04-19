from pages.base_page import BasePage

from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/"

    _FIRST_NAME_FIELD = ("xpath", "//input[@name='firstname']")
    _LAST_NAME_FIELD = ("xpath", "//input[@name='lastname']")
    _EMAIL_FIELD = ("xpath", "//input[@name='email']")
    _RE_ENTER_EMAIL_FIELD = ("xpath", "//input[@name='email_re']")
    _USERNAME_FIELD = ("xpath", "//input[@name='username']")
    _PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    _BIRTHDATE_FIELD = ("xpath", "//input[@name='birthdate']")
    _YEAR_DROPDOWN = ("xpath", "//select[@class='ui-datepicker-year']")
    _MONTH_DROPDOWN = ("xpath", "//select[@class='ui-datepicker-month']")
    _GENDER_CHECKBOX_MALE = ("xpath", "//input[@name='gender' and @value='male']")
    _GENDER_CHECKBOX_FEMALE = ("xpath", "//input[@name='gender' and @value='female']")
    _GDPR_AGREEMENT_CHECKBOX = ("xpath", "//input[@name='gdpr_agree']")
    _CREATE_AN_ACCOUNT_BUTTON = ("xpath", "//input[@value='Create an account']")
    _SUCCESS_REGISTRATION_MESSAGE = ("xpath", "//div[@class='ossn-message-done']")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self._FIRST_NAME_FIELD).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self._LAST_NAME_FIELD).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self._EMAIL_FIELD).send_keys(email)

    def re_enter_email(self, email):
        self.driver.find_element(*self._RE_ENTER_EMAIL_FIELD).send_keys(email)

    def enter_username(self, username):
        self.driver.find_element(*self._USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)

    def choose_birthdate(self, day, month, year):
        self.driver.find_element(*self._BIRTHDATE_FIELD).click()
        Select(self.driver.find_element(*self._YEAR_DROPDOWN)).select_by_value(str(year))
        Select(self.driver.find_element(*self._MONTH_DROPDOWN)).select_by_value(str(month - 1))
        self.driver.find_element("xpath", f"//a[text()='{day}']").click()

    def choose_gender(self, gender):
        if gender == 'male':
            self.driver.find_element(*self._GENDER_CHECKBOX_MALE).click()
        elif gender == 'female':
            self.driver.find_element(*self._GENDER_CHECKBOX_FEMALE).click()
        else:
            raise ValueError("There's no such gender")

    def agree_with_gdpr(self):
        self.driver.find_element(*self._GDPR_AGREEMENT_CHECKBOX).click()

    def click_on_create_an_account_button(self):
        self.driver.find_element(*self._CREATE_AN_ACCOUNT_BUTTON).click()

    def is_success_message_visible(self):
        self.wait.until(EC.visibility_of_element_located(self._SUCCESS_REGISTRATION_MESSAGE),
                        "There's no message about successful registration")
        return self.driver.find_element(*self._SUCCESS_REGISTRATION_MESSAGE).is_displayed()

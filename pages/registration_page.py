from pages.base_page import BasePage

from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):
    PAGE_URL = "https://demo.opensource-socialnetwork.org/"

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstname']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastname']")
    EMAIL_FIELD = ("xpath", "//input[@name='email']")
    RE_ENTER_EMAIL_FIELD = ("xpath", "//input[@name='email_re']")
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    BIRTHDATE_FIELD = ("xpath", "//input[@name='birthdate']")
    YEAR_DROPDOWN = ("xpath", "//select[@class='ui-datepicker-year']")
    MONTH_DROPDOWN = ("xpath", "//select[@class='ui-datepicker-month']")
    GENDER_CHECKBOX_MALE = ("xpath", "//input[@name='gender' and @value='male']")
    GENDER_CHECKBOX_FEMALE = ("xpath", "//input[@name='gender' and @value='female']")
    GDPR_AGREEMENT_CHECKBOX = ("xpath", "//input[@name='gdpr_agree']")
    CREATE_AN_ACCOUNT_BUTTON = ("xpath", "//input[@value='Create an account']")
    SUCCESS_REGISTRATION_MESSAGE = ("xpath", "//div[@class='ossn-message-done']")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def re_enter_email(self, email):
        self.driver.find_element(*self.RE_ENTER_EMAIL_FIELD).send_keys(email)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def choose_birthdate(self, day, month, year):
        self.driver.find_element(*self.BIRTHDATE_FIELD).click()
        Select(self.driver.find_element(*self.YEAR_DROPDOWN)).select_by_value(str(year))
        Select(self.driver.find_element(*self.MONTH_DROPDOWN)).select_by_value(str(month - 1))
        self.driver.find_element("xpath", f"//a[text()='{day}']").click()

    def choose_gender(self, gender):
        if gender == 'male':
            self.driver.find_element(*self.GENDER_CHECKBOX_MALE).click()
        elif gender == 'female':
            self.driver.find_element(*self.GENDER_CHECKBOX_FEMALE).click()
        else:
            raise ValueError("There's no such gender")

    def agree_with_gdpr(self):
        self.driver.find_element(*self.GDPR_AGREEMENT_CHECKBOX).click()

    def click_on_create_an_account_button(self):
        self.driver.find_element(*self.CREATE_AN_ACCOUNT_BUTTON).click()

    def is_success_message_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_REGISTRATION_MESSAGE),
                        "There's no message about successful registration")
        return self.driver.find_element(*self.SUCCESS_REGISTRATION_MESSAGE).is_displayed()

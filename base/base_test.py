from data.credentials import Credentials
from pages.login_page import LoginPage
from pages.news_feed_page import HomePage
from pages.registration_page import RegistrationPage


class BaseTest:

    def setup_method(self):
        self.data = Credentials()
        self.registration_page = RegistrationPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

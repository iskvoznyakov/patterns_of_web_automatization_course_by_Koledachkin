import pytest
import allure
from base.base_test import BaseTest


@allure.epic("Users")
@allure.feature("User Interactions")
@allure.story("Login & Posts")
class TestLoginAndHomePages(BaseTest):

    @allure.title("Login in admin account and publish posts")
    @pytest.mark.parametrize("text", ["Hello World!", "That's my first post", "What's up?"])
    def test_valid_login_and_post(self, text):
        self.login_page.open()
        self.login_page.enter_login(self.data.EXISTING_LOGIN)
        self.login_page.enter_password(self.data.EXISTING_PASSWORD)
        self.login_page.click_login_button()

        self.home_page.posts.create_post(text)
        assert self.home_page.posts.is_post_published(text)

    @allure.title("Invalid login in with wrong credentials")
    def test_invalid_login(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.NON_EXISTING_LOGIN)
        self.login_page.enter_password(self.data.NON_EXISTING_PASSWORD)
        self.login_page.click_login_button()
        assert self.login_page.is_error_message_visible()

    @allure.title("Valid login in imperative way")
    def test_successful_login_imperative(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.EXISTING_LOGIN)
        self.login_page.enter_password(self.data.EXISTING_PASSWORD)
        self.login_page.click_login_button()
        assert self.login_page.driver.current_url == "https://demo.opensource-socialnetwork.org/home"

    @allure.title("Valid login in declarative way")
    def test_successful_login_declarative(self):
        self.login_page.open()
        self.login_page.login_as(self.data.EXISTING_LOGIN, self.data.EXISTING_PASSWORD)
        assert self.login_page.driver.current_url == "https://demo.opensource-socialnetwork.org/home"

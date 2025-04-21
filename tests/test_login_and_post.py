import pytest

from base.base_test import BaseTest


class TestLoginAndHomePages(BaseTest):

    @pytest.mark.parametrize("text", ["Hello World!", "That's my first post", "What's up?"])
    def test_valid_login_and_post(self, text):
        self.login_page.open()
        self.login_page.enter_login("administrator")
        self.login_page.enter_password("administrator")
        self.login_page.click_login_button()

        self.home_page.create_post(text)
        assert self.home_page.is_post_published(text)

    def test_invalid_login(self):
        self.login_page.open()
        self.login_page.enter_login("invalid_user")
        self.login_page.enter_password("invalid_password")
        self.login_page.click_login_button()
        assert self.login_page.is_error_message_visible()

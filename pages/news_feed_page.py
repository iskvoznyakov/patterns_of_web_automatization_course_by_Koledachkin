from base.base_page import BasePage


class HomePage(BasePage):
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/home"

    _POST_FIELD = ("xpath", "//textarea[@name='post']")
    _POST_BUTTON = ("xpath", "//input[@value='Post']")
    _RECENTLY_PUBLISHED_POST = ("xpath", "//div[@post='new']")

    def create_post(self, text):
        self.enter_text(self._POST_FIELD, text)
        self.click(self._POST_BUTTON)

    def is_post_published(self, text):
        return text in self.find_element(self._RECENTLY_PUBLISHED_POST).text

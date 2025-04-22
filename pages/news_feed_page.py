from base.base_page import BasePage
import allure


class HomePage(BasePage):
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/home"

    _POST_FIELD = "//textarea[@name='post']"
    _POST_BUTTON = "//input[@value='Post']"
    _RECENTLY_PUBLISHED_POST = "//div[@post='new']"

    @allure.step("Create post")
    def create_post(self, text):
        self.enter_text(self._POST_FIELD, text)
        self.click(self._POST_BUTTON)

    @allure.step("Check if the post published")
    def is_post_published(self, text):
        return text in self.find_element(self._RECENTLY_PUBLISHED_POST).text

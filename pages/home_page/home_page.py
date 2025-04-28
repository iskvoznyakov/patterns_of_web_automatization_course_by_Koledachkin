from base.base_page import BasePage

from pages.home_page.components.post_block import PostBlock


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.posts = PostBlock(driver)

    _PAGE_URL = "https://demo.opensource-socialnetwork.org/home"

from base.base_test import BaseTest


class TestRegistrationPage(BaseTest):

    def test_registration_of_an_account(self):
        self.registration_page.open()
        self.registration_page.enter_first_name("Ivan")
        self.registration_page.enter_last_name("Ivanov")
        self.registration_page.enter_email("test11@email.ru")
        self.registration_page.re_enter_email("test11@email.ru")
        self.registration_page.enter_username("username")
        self.registration_page.enter_password("password")
        self.registration_page.choose_birthdate(4, 2, 1996)
        self.registration_page.choose_gender("male")
        self.registration_page.agree_with_gdpr()
        self.registration_page.click_on_create_an_account_button()
        assert self.registration_page.is_success_message_visible(), "There's no message about successful registration"

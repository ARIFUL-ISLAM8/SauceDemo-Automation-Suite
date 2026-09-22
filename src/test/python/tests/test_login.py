from base.base_test import BaseTest
from pages.login_page import LoginPage


class TestLogin(BaseTest):

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in self.driver.current_url, "Login failed!"

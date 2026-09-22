from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Page object for the login screen."""

    # Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_username(self, user: str):
        self.driver.find_element(*self.USERNAME).send_keys(user)

    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def login(self, user: str, password: str):
        self.enter_username(user)
        self.enter_password(password)
        self.click_login()

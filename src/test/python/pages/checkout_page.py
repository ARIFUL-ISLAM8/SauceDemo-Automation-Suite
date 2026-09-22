from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Page object for the checkout flow."""

    # Locators
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()

    def enter_details(self, first_name: str, last_name: str, zip_code: str):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BTN).click()

    def get_success_message(self) -> str:
        return self.driver.find_element(*self.SUCCESS_MSG).text

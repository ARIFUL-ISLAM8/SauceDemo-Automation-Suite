from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductPage:
    """Page object for the product listing screen."""

    # Locators
    PRODUCT_TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_product_page_loaded(self) -> bool:
        return self.driver.find_element(*self.PRODUCT_TITLE).is_displayed()

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()

    def get_cart_count(self) -> str:
        return self.driver.find_element(*self.CART_BADGE).text

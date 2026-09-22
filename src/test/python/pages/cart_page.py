from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Page object for the cart screen."""

    # Locators
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(*self.CART_ICON).click()

    def is_item_present(self) -> bool:
        return len(self.driver.find_elements(*self.CART_ITEM)) > 0

    def remove_item(self):
        self.driver.find_element(*self.REMOVE_BTN).click()

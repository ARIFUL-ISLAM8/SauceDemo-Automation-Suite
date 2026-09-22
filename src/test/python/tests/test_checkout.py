from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout(BaseTest):

    def test_complete_checkout(self):
        # Login
        LoginPage(self.driver).login("standard_user", "secret_sauce")

        # Add product & open cart
        ProductPage(self.driver).add_backpack_to_cart()
        CartPage(self.driver).open_cart()

        # Checkout process
        checkout_page = CheckoutPage(self.driver)
        checkout_page.click_checkout()
        checkout_page.enter_details("John", "Doe", "12345")
        checkout_page.click_continue()
        checkout_page.click_finish()

        message = checkout_page.get_success_message()
        assert "Thank you" in message, "Order not completed!"

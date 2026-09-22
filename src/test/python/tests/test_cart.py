from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestCart(BaseTest):

    def test_remove_product_from_cart(self):
        # Login
        LoginPage(self.driver).login("standard_user", "secret_sauce")

        # Add product
        product_page = ProductPage(self.driver)
        product_page.add_backpack_to_cart()

        # Open cart
        cart_page = CartPage(self.driver)
        cart_page.open_cart()

        assert cart_page.is_item_present(), "Item not found in cart!"

        cart_page.remove_item()

        assert not cart_page.is_item_present(), "Item was not removed!"

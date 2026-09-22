from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestProduct(BaseTest):

    def test_add_product_to_cart(self):
        # Login
        LoginPage(self.driver).login("standard_user", "secret_sauce")

        product_page = ProductPage(self.driver)

        assert product_page.is_product_page_loaded(), "Product page not loaded!"

        product_page.add_backpack_to_cart()

        assert product_page.get_cart_count() == "1", "Cart count incorrect!"

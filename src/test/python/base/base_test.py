from selenium import webdriver
import pytest


class BaseTest:
    """Base class providing driver setup and teardown for all tests."""

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

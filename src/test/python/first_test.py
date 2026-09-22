from selenium import webdriver

# Quick smoke test - open saucedemo and print the page title
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

print(f"Page Title: {driver.title}")

driver.quit()

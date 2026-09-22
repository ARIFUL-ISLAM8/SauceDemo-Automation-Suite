from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

print(f"Page Title: {driver.title}")

for i in range(1, 6):
    print(f"i = {i}")

driver.quit()

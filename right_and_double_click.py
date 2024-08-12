"""Program for right click and double click."""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")

actions = ActionChains(driver)
# Locate the element to right-click
right_button = driver.find_element(By.CSS_SELECTOR, "span.context-menu-one")
actions.context_click(right_button).perform()
time.sleep(2)
# Click one of the options of the right button
edit_button = driver.find_element(By.CSS_SELECTOR, "li.context-menu-icon-edit")
actions.context_click(edit_button).perform()
time.sleep(2)
# Accept the alert to close it
driver.switch_to.alert.accept()

# Locate the element to double-click
double_button = driver.find_element(By.XPATH, '//button[text()="Double-Click Me To See Alert"]')
actions.double_click(double_button).perform()
time.sleep(3)
# Switch to the alert
alertText = driver.switch_to.alert.text
# Accept the alert to close it
driver.switch_to.alert.accept()

# Close the driver
driver.quit()


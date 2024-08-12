""" Program for the screenshot."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.google.com")

# Locate the search input field
search_box = driver.find_element(By.NAME, "q")

# Enter the search query
search_box.send_keys("Selenium")
# Submit the search (press Enter)
search_box.send_keys(Keys.RETURN)
time.sleep(5)
driver.save_screenshot("test1.png")

# Close the browser
driver.quit()

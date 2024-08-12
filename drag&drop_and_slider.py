""" Program for Drag and Drop and Slider."""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
# locate the element for drag and drop
source_element = driver.find_element(By.ID, "draggable")
destination_element = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)
# Move to source element and ensure it is visible
driver.execute_script("arguments[0].scrollIntoView();", source_element)
actions.drag_and_drop(source_element, destination_element).perform()

# Locate the element for slider
slider = driver.find_element(By.ID, 'slider')
actions.click_and_hold(slider).move_by_offset(100, 0).release().perform()

time.sleep(7)
driver.quit()

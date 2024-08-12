"""Program for Mouse Hover"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://demo.automationtesting.in/Datepicker.html")

actions = ActionChains(driver)
hover_element = driver.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
actions.move_to_element(hover_element).perform()
time.sleep(2)

driver.find_element(By.XPATH, "//a[normalize-space()='Windows']").click()
time.sleep(3)

driver.quit()

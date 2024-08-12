"""Program to navigate backward and forward."""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://corbah.com/products")
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='shopify-section-header']//li[3]//a[1]").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()

"""Program for Keyboard actions"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.onlinenotepad.io/")
driver.implicitly_wait(10)
#Input text in text area
driver.find_element(By.XPATH, '//*[@id="editorTextarea"]/div[1]').send_keys("Hello Everyone!!")

action = ActionChains(driver)

# Select text ctrl+A
action.key_down(Keys.CONTROL).send_keys("a")
action.key_up(Keys.CONTROL).perform()

# Copy the text ctrl+C
action.key_down(Keys.CONTROL).send_keys("c")
action.key_up(Keys.CONTROL).perform()

# Press the right arrow key
action.send_keys(Keys.ARROW_RIGHT)
time.sleep(2)

#Press the enter key
action.send_keys(Keys.ENTER)

#Paste the text  by ctrl+V
action.key_down(Keys.CONTROL).send_keys("v")
action.key_up(Keys.CONTROL).perform()

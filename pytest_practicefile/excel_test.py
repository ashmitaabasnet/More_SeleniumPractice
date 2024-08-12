import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Function to read data from Excel file
def get_test_data(file_name, sheet_name):
    workbook = openpyxl.load_workbook("test_data.xlsx")
    sheet = workbook["Sheet1"]
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):  # iterates over the rows in sheet, starts from 2nd row.
        data.append((row[0], row[1]))  # Returning tuples for pytest parametrize

    return data

# Parametrizing the test with data from the Excel file
@pytest.mark.parametrize("username, password", get_test_data("test_data.xlsx", "Sheet1"))
def test_login(username, password):
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    # Find the username input field and enter the username
    username_field = driver.find_element(By.ID, "user-name")
    username_field.clear()
    username_field.send_keys(username)

    # Find the password input field and enter the password
    password_field = driver.find_element(By.ID, "password")
    password_field.clear()
    password_field.send_keys(password)

    # Find the login button and click it
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    assert driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed()
    # Close the browser after each test case
    driver.quit()

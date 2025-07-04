import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

@allure.title("Login Test - Practice Test Automation")
@allure.description("This test checks if a user can log in successfully using valid credentials.")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    with allure.step("Open login page"):
        driver.get("https://practicetestautomation.com/practice-test-login/")

    with allure.step("Enter username"):
        username = driver.find_element(By.ID, "username")
        username.send_keys("student")

    with allure.step("Enter password"):
        password = driver.find_element(By.ID, "password")
        password.send_keys("Password123")

    with allure.step("Click submit"):
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

    time.sleep(2)

    with allure.step("Verify login success message"):
        message = driver.find_element(By.TAG_NAME, "h1").text
        assert "Logged In Successfully" in message, "Login Failed"

    with allure.step("Quit browser"):
        driver.quit()

    print("Successfully")

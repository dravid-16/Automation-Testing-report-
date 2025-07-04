import pytest
import allure
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("DemoQA Login Test Using CSV Data")
@allure.description("This test reads multiple login credentials from a CSV file and attempts login to https://demoqa.com/login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_from_csv():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://demoqa.com/login")

    wait = WebDriverWait(driver, 10)

    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['username']
            password = row['password']

            with allure.step(f"Login attempt with username: {username}"):
                user_input = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
                driver.execute_script("arguments[0].scrollIntoView(true);", user_input)
                ActionChains(driver).move_to_element(user_input).perform()
                user_input.clear()
                user_input.send_keys(username)
                allure.attach(username, name="Username", attachment_type=allure.attachment_type.TEXT)

                pass_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
                driver.execute_script("arguments[0].scrollIntoView(true);", pass_input)
                ActionChains(driver).move_to_element(pass_input).perform()
                pass_input.clear()
                pass_input.send_keys(password)
                allure.attach(password, name="Password", attachment_type=allure.attachment_type.TEXT)

                login_button = wait.until(EC.visibility_of_element_located((By.ID, "login")))
                driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
                login_button.click()
                time.sleep(2)

                # After login attempt, navigate back to login for next user
                driver.get("https://demoqa.com/login")

    with allure.step("Close browser"):
        driver.quit()

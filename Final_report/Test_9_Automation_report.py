import pytest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@allure.title("Techlistic Practice Form Automation")
@allure.description("This test fills out the practice form on techlistic.com using Selenium and logs each step with Allure.")
@allure.severity(allure.severity_level.NORMAL)
def test_techlistic_form():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    chrome_options = Options()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    with allure.step("Open Techlistic form page"):
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

    with allure.step("Fill First Name"):
        driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("ATHITHYAN")
        time.sleep(1)

    with allure.step("Fill Last Name"):
        driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("V")
        time.sleep(1)

    with allure.step("Select Gender - Male"):
        driver.find_element(By.XPATH, "//input[@name='sex' and @value='Male']").click()
        time.sleep(1)

    with allure.step("Select Experience - 2 years"):
        driver.find_element(By.XPATH, "//input[@name='exp' and @value='2']").click()
        time.sleep(1)

    with allure.step("Enter Date"):
        driver.find_element(By.ID, "datepicker").send_keys("28/06/2025")
        time.sleep(1)

    with allure.step("Select Profession - Manual Tester"):
        driver.find_element(By.XPATH, "(//input[@name='profession'])[1]").click()
        time.sleep(1)

    with allure.step("Select Automation Tool - Selenium Webdriver"):
        driver.find_element(By.XPATH, "(//input[@name='tool'])[3]").click()
        time.sleep(1)

    with allure.step("Select Continent - Europe"):
        driver.find_element(By.ID, "continents").send_keys("Europe")
        time.sleep(1)

    with allure.step("Quit Browser"):
        driver.quit()

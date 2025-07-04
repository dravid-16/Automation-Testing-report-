import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@allure.title("DemoQA Practice Form Test")
@allure.description("This test fills out the basic fields in the DemoQA form using Selenium.")
@allure.severity(allure.severity_level.CRITICAL)
def test_demoqa_form():
    # Setup Chrome browser
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    with allure.step("Open DemoQA practice form"):
        driver.get("https://demoqa.com/automation-practice-form")

    with allure.step("Fill First Name"):
        driver.find_element(By.ID, "firstName").send_keys("Athithyan")
        allure.attach("Athithyan", name="First Name", attachment_type=allure.attachment_type.TEXT)
        time.sleep(1)

    with allure.step("Fill Last Name"):
        driver.find_element(By.ID, "lastName").send_keys("V")
        allure.attach("V", name="Last Name", attachment_type=allure.attachment_type.TEXT)
        time.sleep(1)

    with allure.step("Fill Email"):
        driver.find_element(By.ID, "userEmail").send_keys("athithyanv402@gmail.com")
        allure.attach("athithyanv402@gmail.com", name="Email", attachment_type=allure.attachment_type.TEXT)
        time.sleep(1)

    with allure.step("Select Gender: Male"):
        driver.find_element(By.XPATH, "//label[text()='Male']").click()
        allure.attach("Male", name="Gender", attachment_type=allure.attachment_type.TEXT)
        time.sleep(1)

    with allure.step("Fill Date of Birth"):
        dob = driver.find_element(By.ID, "dateOfBirthInput")
        dob.clear()
        dob.send_keys("27 Nov 2004")
        allure.attach("27 Nov 2004", name="DOB", attachment_type=allure.attachment_type.TEXT)
        time.sleep(1)

    with allure.step("Close Browser"):
        driver.quit()

    print("Form filled successfully.")
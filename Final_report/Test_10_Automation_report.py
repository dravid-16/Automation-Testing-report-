import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("DemoQA Practice Form Submission Test")
@allure.description("This test fills out basic fields in the DemoQA practice form.")
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_demoqa_form():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    with allure.step("Open DemoQA practice form"):
        driver.get("https://demoqa.com/automation-practice-form")

    with allure.step("Fill First Name"):
        wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Athithyan")
        allure.attach("Athithyan", name="First Name", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Fill Last Name"):
        driver.find_element(By.ID, "lastName").send_keys("V")
        allure.attach("V", name="Last Name", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Fill Email"):
        driver.find_element(By.ID, "userEmail").send_keys("athithyanv402@gmail.com")
        allure.attach("athithyanv402@gmail.com", name="Email", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Fill Mobile Number"):
        driver.find_element(By.ID, "userNumber").send_keys("6494987")
        allure.attach("6494987", name="Mobile Number", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Fill Date of Birth"):
        dob = driver.find_element(By.ID, "dateOfBirthInput")
        dob.clear()
        dob.send_keys("27 Nov 2004")
        allure.attach("27 Nov 2004", name="DOB", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Select Gender: Male"):
        gender_label = driver.find_element(By.XPATH, "//label[text()='Male']")
        driver.execute_script("arguments[0].scrollIntoView(true);", gender_label)
        gender_label.click()
        allure.attach("Male", name="Gender", attachment_type=allure.attachment_type.TEXT)

    time.sleep(2)

    with allure.step("Quit Browser"):
        driver.quit()

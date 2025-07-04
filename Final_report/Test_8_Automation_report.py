import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

@allure.title("JavaScript Alerts Handling Test")
@allure.description("This test handles JS Alert, Confirm, and Prompt dialogs and verifies the result messages.")
@allure.severity(allure.severity_level.CRITICAL)
def test_js_alerts():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # JS Alert
    with allure.step("Handle JS Alert"):
        alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        alert_button.click()
        time.sleep(2)
        alert = driver.switch_to.alert
        allure.attach(alert.text, name="JS Alert Text", attachment_type=allure.attachment_type.TEXT)
        print("Alert Text:", alert.text)
        alert.accept()

        result = driver.find_element(By.ID, "result").text
        print("Result message:", result)
        allure.attach(result, name="JS Alert Result", attachment_type=allure.attachment_type.TEXT)
        assert "You successfully clicked an alert" in result

    # JS Confirm
    with allure.step("Handle JS Confirm (Dismiss)"):
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        allure.attach(alert.text, name="JS Confirm Text", attachment_type=allure.attachment_type.TEXT)
        print("Confirm Text:", alert.text)
        alert.dismiss()
        time.sleep(2)

        result = driver.find_element(By.ID, "result").text
        print("Result message:", result)
        allure.attach(result, name="JS Confirm Result", attachment_type=allure.attachment_type.TEXT)
        assert "You clicked: Cancel" in result

    # JS Prompt
    with allure.step("Handle JS Prompt (Input: ATHITHYAN)"):
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        print("Prompt Text:", alert.text)
        alert.send_keys("ATHITHYAN")
        time.sleep(2)
        alert.accept()
        time.sleep(2)

        result = driver.find_element(By.ID, "result").text
        print("Result message:", result)
        allure.attach(result, name="JS Prompt Result", attachment_type=allure.attachment_type.TEXT)
        assert "You entered: ATHITHYAN" in result

    driver.quit()

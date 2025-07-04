import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

@allure.title("jQuery UI - Drag and Drop Test")
@allure.description("This test performs drag-and-drop inside an iframe and verifies if the drop was successful.")
@allure.severity(allure.severity_level.CRITICAL)
def test_drag_and_drop():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    with allure.step("Open jQuery UI Droppable demo page"):
        driver.get("https://jqueryui.com/droppable/")

    with allure.step("Switch to iframe containing draggable elements"):
        iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
        driver.switch_to.frame(iframe)

    with allure.step("Locate source and target elements"):
        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "droppable")

    with allure.step("Perform drag and drop action"):
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        time.sleep(2)

    with allure.step("Verify drop result"):
        dropped_text = target.text
        allure.attach(dropped_text, name="Droppable Text", attachment_type=allure.attachment_type.TEXT)
        if "Dropped" in dropped_text:
            print("Drag and drop successful")
        else:
            print("Drag and drop failed")
            allure.attach(driver.page_source, name="Page Source", attachment_type=allure.attachment_type.HTML)
            pytest.fail("Drag and drop did not result in expected text")

    driver.quit()

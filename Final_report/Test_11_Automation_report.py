import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.title("DemoQA Menu Hover Test")
@allure.description("This test hovers over multi-level menus on DemoQA and ensures visibility of nested items.")
@allure.severity(allure.severity_level.NORMAL)
def test_menu_hover():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    with allure.step("Open the DemoQA menu page"):
        driver.get("https://demoqa.com/menu")

    with allure.step("Hover over 'Main Item 2'"):
        main_item2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Main Item 2']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", main_item2)
        ActionChains(driver).move_to_element(main_item2).perform()
        time.sleep(1)

    with allure.step("Hover over 'SUB SUB LIST »'"):
        sub_sub_list = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']")))
        ActionChains(driver).move_to_element(sub_sub_list).perform()
        time.sleep(1)

    with allure.step("Hover over 'Sub Sub Item 2'"):
        sub_sub_item2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sub Sub Item 2']")))
        ActionChains(driver).move_to_element(sub_sub_item2).perform()
        time.sleep(1)

    allure.attach("Hovering completed successfully", name="Status", attachment_type=allure.attachment_type.TEXT)
    print("Hovering completed successfully")

    with allure.step("Close the browser"):
        driver.quit()

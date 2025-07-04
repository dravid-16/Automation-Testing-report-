import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

@allure.title("Tab Switching Test")
@allure.description("This test opens Google, then opens Wikipedia in a new tab, switches to it, and prints the title.")
@allure.severity(allure.severity_level.NORMAL)
def test_switch_tabs():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    with allure.step("Open Google homepage"):
        driver.get("https://www.google.com")

    with allure.step("Open Wikipedia in a new tab using JavaScript"):
        driver.execute_script("window.open('https://www.wikipedia.org', '_blank');")

    time.sleep(2)

    with allure.step("Switch to new tab and capture title"):
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        wikipedia_title = driver.title
        print("Title:", wikipedia_title)
        allure.attach(wikipedia_title, name="Wikipedia Page Title", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Close Wikipedia tab"):
        driver.close()

    with allure.step("Switch back to Google tab and close browser"):
        driver.switch_to.window(tabs[0])
        driver.quit()

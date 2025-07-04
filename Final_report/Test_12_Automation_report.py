import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

@allure.title("Browser Navigation Test")
@allure.description("This test navigates between Google and Wikipedia, checks page titles, uses back/forward/refresh, and prints the current URL.")
@allure.severity(allure.severity_level.NORMAL)
def test_browser_navigation():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    with allure.step("Open Google"):
        driver.get("https://www.google.com")
        google_title = driver.title
        print("Opened:", google_title)
        allure.attach(google_title, name="Google Title", attachment_type=allure.attachment_type.TEXT)
        time.sleep(2)

    with allure.step("Navigate to Wikipedia"):
        driver.get("https://www.wikipedia.org")
        wiki_title = driver.title
        print("Opened:", wiki_title)
        allure.attach(wiki_title, name="Wikipedia Title", attachment_type=allure.attachment_type.TEXT)
        time.sleep(2)

    with allure.step("Go back to Google"):
        driver.back()
        time.sleep(2)
        back_title = driver.title
        print("Back to:", back_title)
        allure.attach(back_title, name="Back Title", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Go forward to Wikipedia"):
        driver.forward()
        time.sleep(2)
        forward_title = driver.title
        print("Forward to:", forward_title)
        allure.attach(forward_title, name="Forward Title", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Refresh the page"):
        driver.refresh()
        time.sleep(2)
        refreshed_title = driver.title
        print("Page refreshed:", refreshed_title)
        allure.attach(refreshed_title, name="Refreshed Title", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Get current URL"):
        current_url = driver.current_url
        print("Current URL:", current_url)
        allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Quit browser"):
        driver.quit()

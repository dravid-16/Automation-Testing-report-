import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

@allure.title("Google Search Test")
@allure.description("This test performs a Google search for 'Amazon' and checks if the search executes without error.")
@allure.severity(allure.severity_level.NORMAL)
def test_google_search():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    with allure.step("Open Google homepage"):
        driver.get("https://www.google.com/")
        driver.maximize_window()
        time.sleep(2)

    with allure.step("Find search box and enter 'Amazon'"):
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Amazon")
        allure.attach("Amazon", name="Search Query", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Submit the search"):
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        current_url = driver.current_url
        allure.attach(current_url, name="Search Results URL", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Quit browser"):
        driver.quit()

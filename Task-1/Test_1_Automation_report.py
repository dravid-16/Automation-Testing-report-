import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@allure.title("Open Google Homepage")
@allure.description("This test opens Google's homepage using Selenium WebDriver.")
@allure.severity(allure.severity_level.NORMAL)
def test_open_google():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    with allure.step("Launch Google"):
        driver.get("https://www.google.com/")
        assert "Google" in driver.title

    with allure.step("Quit Browser"):
        driver.quit()

    print("Successfully")



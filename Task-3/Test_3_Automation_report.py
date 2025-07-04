import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

@allure.title("Menu Link Validation Test")
@allure.description("This test clicks on menu links and verifies if the correct page is opened.")
@allure.severity(allure.severity_level.NORMAL)
def test_menu_links_navigation():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    base_url = "https://practicetestautomation.com"
    driver.get(base_url)

    menu_links = {
        "PRACTICE": "practice",
        "BLOG": "blog",
        "COURSES": "courses",
        "CONTACT": "contact"
    }

    for link_text, expected_url_fragment in menu_links.items():
        with allure.step(f"Click on '{link_text}' and verify navigation to '{expected_url_fragment}'"):
            try:
                menu_link = driver.find_element(By.LINK_TEXT, link_text)
                menu_link.click()
                time.sleep(2)
                current_url = driver.current_url
                allure.attach(current_url, name=f"URL after clicking {link_text}", attachment_type=allure.attachment_type.TEXT)

                if expected_url_fragment in current_url:
                    print(f"Opened: {expected_url_fragment}")
                else:
                    print(f"Did not open correctly: {link_text}")
                    allure.attach(driver.page_source, name="Page Source", attachment_type=allure.attachment_type.HTML)
                    pytest.fail(f"Navigation failed for: {link_text}")
            finally:
                driver.get(base_url)

    driver.quit()

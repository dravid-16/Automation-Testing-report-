import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

@allure.title("Dodo App - Menu Navigation Test")
@allure.description("This test clicks on each menu item in Dodo and verifies if the correct URL is opened.")
@allure.severity(allure.severity_level.NORMAL)
def test_dodo_menu_navigation():
    service = Service(r"C:\Users\athi\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    base_url = "https://dodo.quantumnique.tech/"
    driver.get(base_url)

    menu_links = {
        "ASSESSMENTS": "assessments",
        "COURSES": "courses",
        "PRACTICE": "practice",
        "CODE": "code",
        "LSRW": "lsrw",
        "BLOGS": "blog"
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
                    allure.attach(driver.page_source, name=f"Page Source: {link_text}", attachment_type=allure.attachment_type.HTML)
                    pytest.fail(f"Navigation failed for: {link_text}")
            except Exception as e:
                allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"Exception for link: {link_text} - {str(e)}")

    driver.quit()

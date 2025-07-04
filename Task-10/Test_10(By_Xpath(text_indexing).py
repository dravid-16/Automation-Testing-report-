from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open the DemoQA practice form
driver.get("https://demoqa.com/automation-practice-form")

# Fill the form fields using stable locators (ID instead of index-based XPath)
driver.find_element(By.ID, "firstName").send_keys("Athithyan")
time.sleep(1)

driver.find_element(By.ID, "lastName").send_keys("V")
time.sleep(1)

driver.find_element(By.ID, "userEmail").send_keys("athithyanv402@gmail.com")
time.sleep(1)
# Select Gender: Male
driver.find_element(By.XPATH, "//label[text()='Male']").click()
time.sleep(1)

# Date of Birth input
dob = driver.find_element(By.ID, "dateOfBirthInput")
dob.clear()
dob.send_keys("27 Nov 2004")
time.sleep(1)

print("Form filled successfully.")
driver.quit()

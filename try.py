from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service('/Users/savyata/Downloads/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://sauce-demo.myshopify.com/account/login')

wait = WebDriverWait(driver, 50)

# Click Sign up
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[normalize-space()='Sign up']")
)).click()

# Small wait for form to fully load
time.sleep(2)

# First Name
first_name = wait.until(EC.element_to_be_clickable((By.ID, "first_name")))
first_name.click()
first_name.clear()
first_name.send_keys("savyata")

# Last Name
last_name = wait.until(EC.element_to_be_clickable((By.ID, "last_name")))
last_name.click()
last_name.clear()
last_name.send_keys("pandey")

# Email
email = wait.until(EC.element_to_be_clickable((By.ID, "email")))
email.click()
email.clear()
email.send_keys("savyatap@gmail.com")

# Password
password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
password.click()
password.clear()
password.send_keys("pandey123")

# Create account
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//input[@value='Create']")
)).click()

time.sleep(5)
driver.quit()

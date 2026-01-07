from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys # wait import
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service('/Users/savyata/Downloads/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://sauce-demo.myshopify.com/account/login')

#time.sleep(5)
wait=WebDriverWait(driver, 50)

#for signup
# wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Sign up']"))).click()
# firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='first_name']"))).send_keys('savyata')
# lastname=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='last_name']"))).send_keys('pandey')
# email_address=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='email']"))).send_keys("savyatap@gmail.com")
# password=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("pandet123")
# wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@value='Create']"))).click()

#for login
wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Log In']"))).click()
emailaddress=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='customer_email']"))).send_keys("savyatap@gmail.com")
password=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='customer_password']"))).send_keys("pandet123")
button=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@value='Sign In']"))).click()


time.sleep(10)
driver.quit()



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


chrome_options = Options()
chrome_options.add_argument("--start-maximized--")

#for headless and jenkins
chrome_options.add_argument("--headless=new") #this is for run in background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service('/Users/savyata/Downloads/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://sauce-demo.myshopify.com')


def click_element(driver,xpath):
    element = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

def send_keys_to_element(driver, xpath, keys):
    element = driver.find_element(By.XPATH, xpath)
    element.clear() #to clear pahila ko data,
    element.send_keys(keys)

def clear_element(driver,xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.clear()


#call function

LogIn = "//a[normalize-space()='Log In']"
click_element(driver,LogIn)
print("login sucessfully")

Email = "//input[@id='customer_email']"
send_keys_to_element(driver, Email, user_data["email"])

Password = "//input[@id='customer_password']"
send_keys_to_element(driver,Password, user_data["password"])


Email = "//input[@id='customer_email']"
click_element(driver, Email)

Password = "//input[@id='customer_password']"
click_element(driver, Password)

SignIn_button = "//input[@value='Sign In']"
click_element(driver,SignIn_button)


time.sleep(500)
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys # wait import
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized") #built maximized screen

service = Service('/Users/savyata/Downloads/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://sauce-demo.myshopify.com/account/login')

#time.sleep(5)
wait=WebDriverWait(driver, 50) #implict wait

#create function
def click_element(driver,xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()

def send_keys_to_element(driver, xpath, keys):
    element = driver.find_element(By.XPATH, xpath)
    element.clear() #to clear pahila ko data,
    element.send_keys(keys)

def clear_element(driver,xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.clear()


#Call function
SignUp = "//a[normalize-space()='Sign up']"
click_element(driver,SignUp)
print("clicked on signup button") #yo print grya,garda ni huncha nagarda

if "register" in driver.current_url:
    print("Registration form loaded sucscesfully")
else:
    print("Registration from may not loaded properly - current URL:", driver.current_url)

Firstname = "//input[@id='first_name']"
send_keys_to_element(driver,Firstname, "savyata")
print("enter firstname")

LastName= "//input[@id='last_name']"
send_keys_to_element(driver,LastName, "pandey")
print("enter lastname")

#this give same emails always to create
# Email_Address ="//input[@id='email']"
# send_keys_to_element(driver,Email_Address,"savyatap@gmail.com")

#this give unquie email when we created like change num in emails
Email_Address ="//input[@id='email']"
unique_email = f"testuser_{int(time.time())}@gmail.com"
send_keys_to_element(driver, Email_Address, unique_email)
print("email entered")

Password = "//input[@id='password']"
send_keys_to_element(driver,Password,"pandet123")
time.sleep(10)

CreateButton = "//input[@type='submit' and @value='Create']"
click_element(driver, CreateButton)
print("clicked button")

time.sleep(10)

logout_element = driver.find_element(By.XPATH,"//a[text()='Log Out]")
if logout_element:
    print("registration successful- logout element found")
else:
    print("registration unsuccseeful- logout element not found")

#for signup
# wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Sign up']"))).click()  #explict wait,
# firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='first_name']"))).send_keys('savyata')
# lastname=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='last_name']"))).send_keys('pandey')
# email_address=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='email']"))).send_keys("savyatap@gmail.com")
# password=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("pandet123")
# wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@value='Create']"))).click()

#for login
# wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Log In']"))).click()
# emailaddress=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='customer_email']"))).send_keys("savyatap@gmail.com")
# password=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='customer_password']"))).send_keys("pandet123")
# button=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@value='Sign In']"))).click()
#

test_search_data = [

    {
        "email":"sabitra231@gmail.com",
        "password":"Pratik@123",
        "search_term":"Tshirt"

    },
    {
        "email":"savyatapandey@gmail.com",
        "password":"@Test123",
        "search_term":"Jacket"
    },
    {
        "email":"Hari@gmail.com",
        "password":"abc123",
        "search_term":"Pant"
    }

]



time.sleep(10)
driver.quit()



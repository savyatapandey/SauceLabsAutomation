from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


chrome_options = Options()
chrome_options.add_argument("--start-maximized--")

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
        "search_term":"Grey jacket"
    }

]
for i,user_data in enumerate(test_search_data):
    driver.get("https://sauce-demo.myshopify.com")
    time.sleep(3)

#call function

# LogIn = "//a[normalize-space()='Log In']"
# click_element(driver,LogIn)
# print("login sucessfully")
#
# Email = "//input[@id='customer_email']"
# send_keys_to_element(driver, Email, user_data["email"])
#
# Password = "//input[@id='customer_password']"
# send_keys_to_element(driver,Password, user_data["password"])
#
#
# Email = "//input[@id='customer_email']"
# click_element(driver, Email)
#
# Password = "//input[@id='customer_password']"
# click_element(driver, Password)
#
# SignIn_button = "//input[@value='Sign In']"
# click_element(driver,SignIn_button)

search_field = "//input[@id='search-field']"
click_element(driver, search_field)
send_keys_to_element(driver, search_field, "Grey Jacket")
time.sleep(2)

#For add to cart
#first select product
click_product = "//a[@id='product-1']"
click_element(driver, click_product)

#Now add the product to cart
add_to_cart = "//input[@id='add']"
click_element(driver, add_to_cart)

time.sleep(3)

#Now check out
check_out = "//a[@class='checkout']"
click_element(driver, check_out)

check_out_button="//input[@id='checkout']"
click_element(driver,check_out_button)
time.sleep(500)
driver.quit()
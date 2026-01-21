import os.path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import allure

chrome_options = Options()
chrome_options.add_argument("--start-maximized--")

service = Service('/Users/savyata/Downloads/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://sauce-demo.myshopify.com')

#baseclass
@allure.step("click on element with xpath: {xpath}")
def click_element(driver, xpath):
    element = driver.find_element(By.XPATH,xpath)
    assert element.is_displayed(), f"Element with xpath {xpath} is not displayed"
    take_screenshots()
    element.click()
    print(f"Sucessfully clciked on element:{xpath}")

#baseclass
@allure.step("send keys'{keys') to element with xpath: {xpath}")
def send_keys_to_element(driver,xpath,keys):
    element = driver.find_elemet(By.XPATH,keys)
    assert element.is_enabled(), (f"Element with xpath {xpath} is not enabled")
    take_screenshots()
    element.clear()
    element.send_keys()


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


search_field = "//input[@id='search-field']"
click_element(driver, search_field)
if "search result" in driver.current_url:
    print("search page loaded succesfuly loaded")
else:
    print("search page  may not loaded properly - current URL:", driver.current_url)
send_keys_to_element(driver, search_field, "Grey Jacket")
if search_field:
    print("Grey-jacket product should shown")
else:
    print("Grey-jacket product not found")

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


@allure.step("Take screenshot:{name}")
def take_screenshots(self, name="screenshot",timestamp=True):
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    import time
    if timestamp:
        timestamp_str = int(time.time())
        filename = f"{screenshots_dir}/{name}_{timestamp_str}.png"
    else:
        filename = f"{screenshots_dir}/{name}.png"
    self.driver.save_screenshot(filename)

    allure.attach.file(
        filename,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
    print(f"Screenshot taken:{filename}")



driver.quit()
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

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

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
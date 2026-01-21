# import os
# import time
# import pytest
# import allure
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # --- Helper functions for Allure steps ---
#
# @allure.step("Click on element with xpath: {xpath}")
# def click_element(driver, xpath):
#     wait = WebDriverWait(driver, 10)
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
#     element.click()
#
# @allure.step("Send keys '{keys}' on element with xpath: {xpath}")
# def send_keys_to_element(driver, xpath, keys):
#     wait = WebDriverWait(driver, 10)
#     element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
#     element.clear()
#     element.send_keys(keys)
#
# def take_screenshot(driver, name):
#     screenshots_dir = "screenshots"
#     if not os.path.exists(screenshots_dir):
#         os.makedirs(screenshots_dir)
#
#     timestamp = int(time.time())
#     filename = f"{screenshots_dir}/{name}_{timestamp}.png"
#     driver.save_screenshot(filename)
#
#     allure.attach.file(
#         filename,
#         name=name,
#         attachment_type=allure.attachment_type.PNG
#     )
#
# # --- Pytest Fixture for Driver Management ---
#
# @pytest.fixture
# def driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     # Update this path to your actual chromedriver location
#     service = Service('/Users/savyata/Downloads/chromedriver-mac-arm64/chromedriver')
#
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     yield driver
#     driver.quit()
#
# # --- The Test Case ---
#
# @allure.feature("Shopping Cart")
# @allure.story("Search and Add to Cart")
# @pytest.mark.parametrize("user_data", [
#     {"search_term": "Grey Jacket", "path": "//h3[normalize-space()='Grey jacket']"},
#     {"search_term": "Black heels", "path": "//h3[normalize-space()='Black heels']"},
#     {"search_term": "Brown Shades", "path": "//h3[normalize-space()='Brown Shades']"}
# ])
# def test_sauce_demo_search(driver, user_data):
#     """
#     This test runs separately for each item in the parametrization list.
#     """
#     # Selectors
#     SEARCH_FIELD = "//input[@id='search-field']"
#     SEARCH_SUBMIT = "//input[@id='search-submit']"
#     ADD_TO_CART = "//input[@id='add']"
#     CHECKOUT_BTN = "//a[normalize-space()='Check Out']"
#
#     try:
#         with allure.step(f"Testing search for: {user_data['search_term']}"):
#             driver.get('https://sauce-demo.myshopify.com/')
#
#             # Perform Search
#             click_element(driver, SEARCH_FIELD)
#             send_keys_to_element(driver, SEARCH_FIELD, user_data['search_term'])
#             click_element(driver, SEARCH_SUBMIT)
#
#             # Select Product
#             click_element(driver, user_data['path'])
#
#             # Add to Cart
#             click_element(driver, ADD_TO_CART)
#
#             # Go to Checkout
#             click_element(driver, CHECKOUT_BTN)
#
#             # Verify result with a screenshot
#             take_screenshot(driver, f"Result_{user_data['search_term'].replace(' ', '_')}")
#
#     except Exception as e:
#         take_screenshot(driver, "Failure_Screenshot")
#         pytest.fail(f"Test failed for {user_data['search_term']}: {e}")
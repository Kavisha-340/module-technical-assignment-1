from dotenv import load_dotenv
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "BROWSERSTACK_USERNAME"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "BROWSERSTACK_ACCESS_KEY"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"

bstack_options = {
    "os" : "OS X",
    "osVersion" : "Ventura",
    "buildName" : "module-technical-assignment-1",
    "sessionName" : "BStack single python",
    "userName": BROWSERSTACK_USERNAME,
    "accessKey": BROWSERSTACK_ACCESS_KEY
}

options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor=URL,
    options=options)

try:
    driver.get("https://bstackdemo.com/")
    
    # Find the sign-in button and click on it
    signin_btn = driver.find_element(By.CSS_SELECTOR, '#signin')
    signin_btn.click()
    driver.implicitly_wait(5)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-btn")

    # Select demouser as Username
    username.click()
    username_input = driver.find_element(By.CSS_SELECTOR, "#react-select-2-option-0-0")
    username_input.click()

    # Select testingisfun99 as Password
    password.click()
    password_input = driver.find_element(By.CSS_SELECTOR, "#react-select-3-option-0-0")
    password_input.click()

    # Submit the form
    login_btn.click()
    driver.implicitly_wait(10)

    # Click the 'Add to cart' button if it is visible
    add_to_cart_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/div[4]')))
    add_to_cart_btn.click()
    
    # Check if the cart pane is visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart__content")))

    # Click the Checkout button
    checkout_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[3]/div[3]')))
    checkout_btn.click()
    driver.implicitly_wait(5)
    
    # Check if the form is visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout-app"]/div/div/aside/article/header/h3')))
    
    # Fill the form
    first_name = driver.find_element(By.CSS_SELECTOR, '#firstNameInput')
    last_name = driver.find_element(By.CSS_SELECTOR, '#lastNameInput')
    address = driver.find_element(By.CSS_SELECTOR, '#addressLine1Input')
    state = driver.find_element(By.CSS_SELECTOR, '#provinceInput')
    pincode = driver.find_element(By.CSS_SELECTOR, '#postCodeInput')

    first_name.send_keys('Kavisha')
    last_name.send_keys('Gupta')
    address.send_keys('Prayagraj')
    state.send_keys('UP')
    pincode.send_keys('123456')

    # Click the submit button if it is visible
    submit_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout-shipping-continue"]')))
    submit_btn.click()
    driver.implicitly_wait(5)

    # Find the confirmation message
    confirm_msg = driver.find_element(By.XPATH, '//legend[@id="confirmation-message"]')

    # Check if confirmation message is displayed
    if confirm_msg.is_displayed() == True:
        # Set the status of test as 'passed' if confirmation message is displayed
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Your order has been placed successfully"}}')
    else:
        # Set the status of test as 'failed' if confirmation message is not displayed
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Oops! Please try again after some time"}}')

except NoSuchElementException as err:
    message = "Exception: " + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

except Exception as err:
    message = "Exception: " + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

driver.quit()
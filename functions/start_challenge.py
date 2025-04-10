import xpath
from selenium.webdriver.common.by import By

def start_challenge(driver):
    _start_challenge = driver.find_element(By.XPATH, xpath.BUTTON_START)
    _start_challenge.click()
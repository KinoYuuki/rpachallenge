import xpath
from selenium.webdriver.common.by import By

def submit_forms(driver):
    _submit_forms = driver.find_element(By.XPATH, xpath.BUTTON_SUBMIT)
    _submit_forms.click()
from selenium.webdriver.common.by import By

def fill_input(driver, value, xpath):
    input = driver.find_element(By.XPATH, xpath)
    input.clear()
    input.send_keys(value)
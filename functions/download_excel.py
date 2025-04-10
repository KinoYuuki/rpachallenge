import os, variables, xpath
from time import sleep

from selenium.webdriver.common.by import By


def download_excel(driver):
    if not os.path.exists(variables.EXCEL_PATH):
        _download_excel = driver.find_element(By.XPATH, xpath.BUTTON_DOWNLOAD)
        _download_excel.click()
        while not os.path.exists(variables.EXCEL_PATH):
            sleep(0.5)
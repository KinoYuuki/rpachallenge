from selenium import webdriver
from time import sleep
from functions import download_excel, start_challenge, submit_forms, fill_input
import variables, xpath, os
import pandas as pd

driver = webdriver.Chrome()
driver.get(variables.URL)

download_excel(driver)

df = pd.read_excel(variables.EXCEL_PATH, engine="openpyxl")

start_challenge(driver)

for i in range(0, 10):
    fill_input(driver, df["First Name"][i], xpath.INPUT_FIRST_NAME)
    fill_input(driver, df["Last Name "][i], xpath.INPUT_LAST_NAME)
    fill_input(driver, df["Company Name"][i], xpath.INPUT_COMPANY)
    fill_input(driver, df["Role in Company"][i], xpath.INPUT_ROLE)
    fill_input(driver, df["Address"][i], xpath.INPUT_ADDRESS)
    fill_input(driver, df["Email"][i], xpath.INPUT_EMAIL)
    fill_input(driver, str(df["Phone Number"][i]), xpath.INPUT_PHONE)

    submit_forms(driver)

os.remove(variables.EXCEL_PATH)
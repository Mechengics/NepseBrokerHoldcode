from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import re
import math

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.page_load_strategy = 'eager'
# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

# Load the initial URL
url1 = "https://www.sharesansar.com/company/uslb"
driver.get(url1)
# Read the CSV file and set column names
indexnames = [0, 1]
emptyfilled = pd.read_csv("pricehistoryuslb.csv")
emptyfilled.columns = indexnames
df0 = pd.DataFrame()
buttonxapth1 = '//*[@id="btn_cfloorsheet"]'
button1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, buttonxapth1)))
button1.click()
sleep(10)
b = 0
for index, row in emptyfilled.iterrows():
    inputdatexpath = '//*[@id="date"]'
    inputdate = driver.find_element(By.XPATH, inputdatexpath)
    inputdate.clear()
    inputdate.send_keys(str(row[1]))
    buttonxpath2 = '//*[@id="btn_flsheet_submit"]'
    button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, buttonxpath2)))
    button2.click()
    sleep(3)
    findingentries = driver.find_element(By.XPATH, '//*[@id="myTableCFloorsheet_info"]')
    match1 = re.search(r'(\d+)\D*entries', findingentries.text)
    last_entry = match1.group(1) if match1 else "No number found"
    loopmain = int(last_entry) / 500
    print(math.floor(loopmain))
    if int(loopmain) < 1:
        select_element1 = driver.find_element(By.XPATH, '//*[@id="myTableCFloorsheet_length"]/label/select')
        select1 = Select(select_element1)
        select1.select_by_value("500")
        sleep(3)
        htmlsource2 = driver.page_source
        soup2 = BeautifulSoup(htmlsource2, 'html.parser')
        tab1 = pd.read_html(str(soup2))
        newdataframe = pd.DataFrame(tab1[6])
        df0 = pd.concat([newdataframe.reset_index(drop=True), df0.reset_index(drop=True)], axis=0)
        print(df0)
        df0.to_csv("DataCollectiondummy.csv")
        b += 1
        sleep(3)
    else:
        for _ in range((math.floor(loopmain) + 1)):
            select_element1 = driver.find_element(By.XPATH, '//*[@id="myTableCFloorsheet_length"]/label/select')
            select1 = Select(select_element1)
            select1.select_by_value("500")
            sleep(3)
            htmlsource2 = driver.page_source
            soup2 = BeautifulSoup(htmlsource2, 'html.parser')
            tab1 = pd.read_html(str(soup2))
            newdataframe = pd.DataFrame(tab1[6])
            df0 = pd.concat([newdataframe.reset_index(drop=True), df0.reset_index(drop=True)], axis=0)
            print(len(df0))
            df0.to_csv("DataCollectiondummy.csv")
            btn_css = '#myTableCFloorsheet_next'
            btn_next = driver.find_element(By.CSS_SELECTOR, '#myTableCFloorsheet_next')
            btn_next.click()
            b += 1
driver.quit()

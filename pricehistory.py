from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
url1="https://www.sharesansar.com/company/uslb"
driver.get(url1)
buttonxapth='//*[@id="btn_cpricehistory"]'
button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, buttonxapth)))
button.click()
sleep(4)
select_element = driver.find_element(By.XPATH, '//*[@id="myTableCPriceHistory_length"]/label/select')
select = Select(select_element)
select.select_by_value("50")
sleep(3)
htmlsource1=driver.page_source
path='//*[@id="myTableCPriceHistory_paginate"]/span/a[6]'
element=driver.find_element(By.XPATH, path)
text=element.text.strip()
i=0
print(text)
emptyfilled=pd.DataFrame()
for _ in range(int(text)):
    select_element = driver.find_element(By.XPATH, '//*[@id="myTableCPriceHistory_length"]/label/select')
    select = Select(select_element)
    select.select_by_value("50")
    sleep(3)
    htmlsource1=driver.page_source
    soup=BeautifulSoup(htmlsource1, 'html.parser')
    i=i+1
    filename="html" +str(i)+".html"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(soup))
    tab="table"+str(i)
    tab=pd.read_html(filename)
    date="Dateraw"+str(i)
    date=pd.DataFrame(tab[6])
    emptyfilled=pd.concat([emptyfilled, date["Date"]])
    nextbuttonxpath='//*[@id="myTableCPriceHistory_next"]'
    next=driver.find_element(By.XPATH, nextbuttonxpath)
    next.click()
    sleep(3)
    emptyfilled.to_csv("pricehistoryuslb.csv")

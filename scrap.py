from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
browser = webdriver.chrome ("C:/Users/Xervice861/OneDrive/Desktop/web data extraction/chromedriver.exe")
browser.get(START_URL) 
time.sleep(10)
scrape_data=[]

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table  = soup.find("table",attrs ={"class","wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    
    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols) 
        temp_list = []
        for col_data in table_cols:
            #print(col_data.text)
            data = col_data.text.strip()
            temp_list.append(data)
    scrape_data.append (temp_list)
stars_data = []

for i in range(0,len(scrape_data)):
    star_names = scrape_data[i][1]
    Distance = scrape_data[i][3]
    Mass = scrape_data[i][5]
    Radius = scrape_data[i][6]
    Lum = scrape_data[i][7]
    
    required_data = [star_names, Distance,Mass,Radius,Lum]
    stars_data.append(required_data)
    
    headers = ['Star_name','Distance','Mass','Radius','Luminosity']
    
    star_df_1 = pd.DataFrame(stars_data,columns = headers)
    star_df_1.to_csv('Scraped_data.csv',index = True,index_label="id")
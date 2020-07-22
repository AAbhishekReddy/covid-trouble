from selenium import webdriver as wb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import re
import time

print("Target Aquired")

d = wb.Chrome("E:\Code dump\covid\data\chromedriver.exe")

d.get("https://www.worldometers.info/coronavirus/")

print("\nWe are in....\n\nWelcome GHOST\n")

try:
    d.find_element_by_xpath('/html/body/div[1]/div/a').click()
    d.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/ul/li[1]/a').click()    
except Exception as e:
    print(e)
    print("Its out of the way.")

# Columns drop down
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/button").click()
# Selecting the columns
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/ul/li[6]/div/label/input").click()
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/ul/li[14]/div/label/input").click()
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/ul/li[15]/div/label/input").click()
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/ul/li[16]/div/label/input").click()
# Closing the columns drop down
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/button").click()

table = []
flag = 0

# Scrapping the cells one by one.
print("\nExtracting......\n")
for i in range(3, 224):
    row = []
    try:
        if len(d.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr[' + str(i) + ']').text) > 0:
            flag = 1
            row.append(d.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr[' + str(i) + ']/td[1]').text)
            row.append(d.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr[' + str(i) + ']/td[2]').text)
            for j in range(3, 20):
                rec = d.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr[' + str(i) + ']/td[' + str(j) + ']').text
                if '+' in rec:
                    rec = rec.replace('+', '')
                if ',' in rec:
                    rec = rec.replace(',', '')
                if len(rec) is 0:
                    rec = '0'
                try:
                    rec = int(rec)
                except Exception as e:
                    print(e)
                    rec = float(rec)
                    print("handled")
                row.append(rec)
            row[16] = d.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr[' + str(i) + ']/td[16]').get_attribute('data-continent')
        
        if flag == 1:
            table.append(row)
            flag = 0
    except Exception as e:
        print(e)

print("\nDone.\n")

print("\nCreating a dataframe.....\n")
# Data frame creation
col = ["#", "Country", "Total Cases", "New Cases", "Total Deaths",
        "New Deaths", "Total Recovered", "New Recovered", "Active Cases", 
        "Serious Critical", "Tot Cases/ 1M pop", "Deaths/ 1M pop", "Total Tests",
        "Tests/ 1M pop", "Population", "1 Cases every X ppl", "1 Death every X ppl", "1 test every X ppl", "Country"]

world = pd.DataFrame(table, columns = col)
print("\n WORLD created.\n")
import pandas as pd
from selenium import webdriver as wb
import numpy as np
import re

d = wb.Chrome("E:\Code dump\covid\data\chromedriver.exe")

d.get("https://www.worldometers.info/coronavirus/")

# Columns drop down
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/button").click()
# Selecting the columns
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/ul/li[6]/div/label/input").click()
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/ul/li[14]/div/label/input").click()
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/ul/li[15]/div/label/input").click()
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/ul/li[16]/div/label/input").click()
# Closing the columns drop down
d.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[3]/ul/div/button").click()


# retrieving the values from the table.
test = d.find_element_by_id("main_table_countries_today")
table = test.text

# Opening a file to write and check the data.
# f = open("test.txt", "a")
# f.write(table)
# f.close

table = table.split("\n")

del table[0:18]
del table[215]

col = ["#", "Country", "Total Cases", "New Cases", "Total Deaths",
        "New Deaths", "Total Recovered", "New Recovered", "Active Cases", 
        "Serious Critical", "Tot Cases/ 1M pop", "Deaths/ 1M pop", "Total Tests",
        "Tests/ 1M pop", "Population", "Cases every X ppl", "1 Death every X ppl", "test every X ppl"]


for i in range(0, len(table)):
    # print(i)
    # string = table[i]
    # print(string)
    try:
        country = re.findall(r'[A-Z][a-z]+[-]+[A-Z][a-z]', table[i])
        # print("lol")
        if len(country) > 0:
            new = country[0].replace('-', '')
            table[i] = re.sub('[A-Za-z]+[-]+[A-Za-z]+', new, table[i])

        country = re.findall(r'[a-zA-Z]+\.', table[i])
        if len(country) > 0:
            new = country[0].replace('.', '')
            table[i] = re.sub('[a-zA-Z]+\.', new, table[i])

        country = re.findall(r'[a-zA-Z]+', table[i])
        name = ""
        copy = ""
        if len(country) > 1:
            for j in country:
                name = name + j
                copy = copy + j + " "
            table[i] = table[i].replace(copy, name + " ")
        
        table[i] = table[i].split(" ")
        for k in [3,5]:
            if (table[i][k][0] is not '+'):
                table[i].insert(k, '0')
        if table[i][7][0] is not "N":
            if (table[i][7][0] is not '+'):
                table[i].insert(7, '0')
    except IndexError:
        print(table[i])


        # /html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]/tr[3]/td[2]
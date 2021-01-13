# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:14:27 2021

@author: Johnny_Huang
"""

# from selenium import webdriver

# driver=webdriver.Chrome("D:\python\selenium\chromedriver.exe")
# driver.get('http://www.cfd.tw/index.php')

# element=driver.find_element_by_name("LoginName")
# element.send_keys("scofm02356")

# element2=driver.find_element_by_name("LoginPass")
# element2.send_keys("49340368")

# button=driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr/td[5]/div/div[1]/div[2]/form/div[5]/div[2]/input")
# button.click()

from openpyxl import load_workbook

wb = load_workbook(r'D:\\python\\selenium\\料號申請控管-2020.xlsx')
sheet = wb.active 
b4 = sheet['B500']

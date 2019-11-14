# -*- coding: utf-8 -*-
# __author__ = "maple"



import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://pythonav.com/login/')
driver.find_element_by_id('id_username').send_keys('张绍华')
driver.find_element_by_id('id_username').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id('id_username').send_keys(Keys.CONTROL, 'c')
time.sleep(3)

driver.find_element_by_id('id_code').send_keys(Keys.CONTROL, 'v')
time.sleep(3)
# driver.find_element_by_id('id_code').send_keys(Keys.F5)
# time.sleep(3)
driver.quit()













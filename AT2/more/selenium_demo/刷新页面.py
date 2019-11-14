# -*- coding: utf-8 -*-
# __author__ = "maple"


import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    driver.get('https://pythonav.com/login/')
    driver.find_element_by_id('id_username').send_keys('2222222222')
    driver.find_element_by_id('id_password').send_keys('222222222222222')
    driver.find_element_by_xpath('//*[@id="fm"]/div[5]/div/input').click()
    res = driver.find_element_by_xpath('//*[@id="fm"]/div[3]/div/div[1]/span').text
    if res:
        driver.save_screenshot('error.png')
    time.sleep(3)
    # 刷新页面
    driver.refresh()
except Exception:
    pass
finally:
    time.sleep(3)
    driver.quit()
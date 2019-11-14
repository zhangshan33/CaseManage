# -*- coding: utf-8 -*-
# __author__ = "maple"
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
try:
    time.sleep(2)
    driver.find_element_by_id('kw').send_keys('听雨危楼 博客园')
    time.sleep(2)
    driver.find_element_by_id('su').click()
    time.sleep(2)
    driver.find_element_by_link_text('听雨危楼 - 博客园').click()
    time.sleep(1)
    res = driver.window_handles
    print(11111111, res)
    print(22222222, driver.current_window_handle)
    driver.switch_to.window(res[-1])
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mainContent"]/div/div[1]/div[2]/a').click()
    time.sleep(1)
    driver.switch_to.window(res[0])
    print(driver.title)
    # driver.switch_to.frame()
    # driver.switch_to.default_content()
except Exception as e:
    print(e)

finally:
    time.sleep(2)
    driver.quit()
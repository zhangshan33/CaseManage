# -*- coding: utf-8 -*-
# __author__ = "maple"
# import time
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(time_to_wait=10)
# driver.get('https://www.baidu.com')
# driver.find_element_by_id("kw").send_keys("听雨危楼-cnblogs")
# driver.find_element_by_id("su").click()
#
# # time.sleep(2)
# # driver.find_element_by_link_text("听雨危楼 - 博客园").click()
#
# # WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.LINK_TEXT, '听雨危楼 - 博客园'))).click()
# # WebDriverWait(driver, timeout=10).until(EC.invisibility_of_element((By.LINK_TEXT, '听雨危楼 - 博客园')))
#
#
#
#
#
#
#
# time.sleep(2)
# driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.implicitly_wait(time_to_wait=10)
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
driver.get('https://www.baidu.com')
driver.find_element_by_id("kw").send_keys("听雨危楼-cnblogs")
driver.find_element_by_id("su").click()

# time.sleep(2)
# driver.find_element_by_link_text("听雨危楼 - 博客园").click()

# WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.LINK_TEXT, '听雨危楼 - 博客园'))).click()
# WebDriverWait(driver, timeout=10).until(EC.invisibility_of_element((By.LINK_TEXT, '听雨危楼 - 博客园')))

wait.until(EC.presence_of_element_located((By.LINK_TEXT, '听雨危楼 - 博客园'))).click()





time.sleep(2)
driver.quit()

















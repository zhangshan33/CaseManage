# -*- coding: utf-8 -*-
# __author__ = "maple"


import time
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get('https://www.baidu.com')
    # 首先send 一些值
    driver.find_element_by_id('kw').send_keys('我不管我最帅！')
    # 法1 通过attr获取value值，这里有需要说明，该方法必须保证input框有value属性才能用
    time.sleep(1)
    result1 = driver.execute_script('return $("#kw").attr("name");')  # 但这种方式获取别的就很正常
    print(result1)
    # 法2 通过 val获取
    time.sleep(1)
    result2 = driver.execute_script('return $("#kw").val();')
    print(result2)
    # 法3 通过selenium的 get_attribute 获取
    time.sleep(1)
    result3 = driver.find_element_by_id('kw').get_attribute('value')
    print(result3)
    driver.execute_script('alert("{}")'.format(result3))

finally:
    time.sleep(10)
    driver.quit()
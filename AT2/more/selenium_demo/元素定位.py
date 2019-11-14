# -*- coding: utf-8 -*-
# __author__ = "maple"

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
# driver.get(url='https://www.baidu.com')
driver.get(url='http://127.0.0.1:8033/test/')
# driver.get(url='https://www.luffycity.com/home')

# 通过id定位
def find_id():
    driver.get(url='https://pythonav.com/login/')  # 你想访问什么url
    driver.find_element_by_id('id_username').send_keys('虎哥')
    time.sleep(3)
    driver.find_element_by_id('id_password').send_keys('dsb')

def find_class():
    driver.get(url='https://www.baidu.com/')  # 你想访问什么url
    time.sleep(3)
    driver.find_element_by_id('kw').send_keys('帅哥')
    driver.find_element_by_id('kw').send_keys(Keys.ENTER)
    time.sleep(2)
    print(driver.find_element_by_class_name('s_tab_inner').text)


    # driver.get(url='https://pythonav.com/login/')
    # time.sleep(2)
    #
    # input_list = driver.find_elements_by_class_name('form-control')
    # # print(input_list)
    # for i in input_list:
    #     i.send_keys('22323')

def find_text(driver):
    time.sleep(2)
    driver.find_element_by_id('kw').send_keys('听雨危楼 博客园')
    time.sleep(2)
    driver.find_element_by_id('su').click()
    time.sleep(2)
    driver.find_element_by_link_text('听雨危楼 - 博客园').click()

def find_partial():
    time.sleep(2)
    # driver.find_element_by_partial_link_text('模糊').click()
    driver.find_element_by_link_text('模糊定位').click()

def find_xpath():
    time.sleep(2)
    driver.find_element_by_id('kw').send_keys('听雨危楼 博客园')
    time.sleep(2)
    driver.find_element_by_id('su').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()

def find_css():
    time.sleep(2)
    res = driver.find_element_by_css_selector('div[class="d"]').text
    print(res)

def find_tag():
    time.sleep(2)
    # res = driver.find_element_by_tag_name('div').text
    # print(res)

def find_name_method():
    time.sleep(2)
    # res = driver.find_element_by_tag_name('div').text
    # print(res)
    driver.find_element_by_name('a').send_keys('1111111111111')





if __name__ == '__main__':
    # find_id()
    # find_class()
    # find_text(driver)
    # find_xpath()
    # find_css()
    # find_tag()
    # find_name_method()
    find_partial()
    time.sleep(3)
    driver.quit()

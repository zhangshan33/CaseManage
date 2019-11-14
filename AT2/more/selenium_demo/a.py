# -*- coding: utf-8 -*-
# __author__ = "张开"
# 2019/9/24

'''
pip install -i https://pypi.doubanio.com/simple/ selenium
'''
import time
from selenium import webdriver  # 浏览器驱动
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待事件
from selenium.webdriver.common.by import By  # 选择器，以什么方式选择标签元素
driver = webdriver.Chrome()  # 实例化谷歌浏览器对象

# driver.get(url='https://pythonav.com/login/')   # 你想访问什么url
# driver.get('https://www.taobao.com')
# driver.get('http://www.sina.com.cn/')
# # 获取当前URL的title
# # print(driver.title)
# try:
#     # 获取当前URL的title
#     # print(driver.title)
#     # print(driver.get_cookies())  # 获取cookies
#     # print(driver.current_url)  # 当前的url
#     # print(driver.page_source)   # 当前的页面内容
#     # driver.maximize_window()  # 窗口最大化
#     # time.sleep(1)
#     # driver.minimize_window()  #  窗口最小化
#     # time.sleep(2)
#     # driver.maximize_window()
#     # print(driver.current_window_handle)  # 当前的窗口对象
#     # driver.close()  # 关闭当前的窗口对象
#     # print(driver.name)  # 当前浏览器名字
#     # print(driver.find_element_by_id('app').text)
#     # 找到输入框
#     # input_obj = driver.find_element_by_id('kw')
#     # input_obj.send_keys('美女')  # 输入内容
#     # time.sleep(2)
#     # input_obj.send_keys(Keys.ENTER)
#     # 点击搜索标签
#     # submit_obj = driver.find_element_by_id('su')
#     # submit_obj.click()
#     # time.sleep(2)
#     # EC.presence_of_element_located((By.LINK_TEXT,"美女_百度图片"))(driver)
#     # driver.find_element_by_link_text('美女_百度图片').click()
#
#     # driver.back()
#     # time.sleep(2)
#     # driver.forward()   # 前进
#     # time.sleep(2)
#     # driver.back()  # 后退
#     # time.sleep(2)
#     # driver.close()
#     driver.execute_script('alert("xxoo")')  # 执行js代码
#
# # except Exception as e:
# #     time.sleep(2)
# #     driver.quit()  # 无论如何，退出浏览器
# finally:
#     time.sleep(5)
#     driver.quit()  # 无论如何，退出浏览器


# 通过id定位
# def find_id():
#     driver.get(url='https://pythonav.com/login/')  # 你想访问什么url
#     driver.find_element_by_id('id_username').send_keys('虎哥')
#     time.sleep(3)
#     driver.find_element_by_id('id_password').send_keys('dsb')


def find_class():
    driver.get(url='https://www.baidu.com/')  # 你想访问什么url
    # time.sleep(3)
    # driver.find_element_by_id('kw').send_keys('帅哥')
    # driver.find_element_by_id('kw').send_keys(Keys.ENTER)
    # time.sleep(2)
    # print(driver.find_element_by_class_name('s_tab_inner').text)


    # driver.get(url='https://pythonav.com/login/')
    # time.sleep(2)
    #
    # input_list = driver.find_elements_by_class_name('form-control')
    # # print(input_list)
    # for i in input_list:
    #     i.send_keys('22323')


if __name__ == '__main__':
    # find_id()
    find_class()
    driver.refresh()
    driver.save_screenshot('error.png')
    time.sleep(3)
    driver.quit()














































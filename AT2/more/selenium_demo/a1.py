# -*- coding: utf-8 -*-
# __author__ = "maple"


from selenium import webdriver   # 浏览驱动

driver = webdriver.Chrome()   # 获取浏览器驱动对象

driver.get(url='https://www.baidu.com')

# 窗口最大化、最小化
# driver.maximize_window()
# driver.minimize_window()

# driver.forward()  # 前进
# driver.back()   # 后退

# driver.current_window_handle   # 当前的窗口对象
# driver.current_url   # 当前页面的url
# print(driver.title)   # 当前页面的title
# driver.name   # 浏览器对象
# driver.close()   # 关闭当前窗口

# driver.page_source   # 获取当前页的html
# driver.get_cookies()  # 获取cookies
# print(driver.get_window_size())   # {'width': 1050, 'height': 708}
# driver.quit()   # 退出整个浏览器














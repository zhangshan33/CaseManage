# coding:gbk
# class B: pass
# class A(B):
#
#
#     __name = 'abc'
#     def __init__(self, name='bc'):
#         self.name = name
#     def foo(self, *args, **kwargs):pass
# a = A('W')
# a.age = 18


# a.foo = foo
# print(A.__dict__)
# print(a.__dict__)
# print(a._A__name)
# print(A.mro())


# --------------- 获取屏幕的大小 ---------------
# from appium import webdriver
#
# desired_caps = {
#     "platformName": "android",
#     "platformVersion": "4.4.2",
#     "deviceName": "127.0.0.1:62025",
#     "appPackage": "com.jd.app.reader",
#     "appActivity": "com.jingdong.app.reader.logo.JdLogoActivity"
# }
#
# driver = webdriver.Remote('http://127.0.0.1:4700/wd/hub', desired_caps)
# print(driver.get_window_size())  # {'width': 720, 'height': 1280}
# print(driver.get_window_size()['width'])  # 720
# print(driver.get_window_size()['height'])  # 1280


# --------------------- 通过id定位 -------------------

# import time
# from appium import webdriver
#
# desired_caps = {
#     "platformName": "android",
#     "platformVersion": "4.4.2",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.jd.app.reader",
#     "appActivity": "com.jingdong.app.reader.logo.JdLogoActivity",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True
#
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# # 点击跳过首页广告
# driver.find_element_by_id('com.jd.app.reader:id/skip_tv').click()
# time.sleep(1)
# # 点击顶部的输入框
# driver.find_element_by_id('com.jd.app.reader:id/mSearchLayout').send_keys()
# time.sleep(1)
# # 在新的搜索页面输入值
# driver.find_element_by_id('com.jd.app.reader:id/mSearchKeyInput').send_keys('上古卷轴')
# time.sleep(1)
# # 有了值，就可以点击搜索按钮进行搜索
# driver.find_element_by_id('com.jd.app.reader:id/mSearchBtn').click()

# --------------------- 通过class定位 -------------------

# import time
# from appium import webdriver
#
# desired_caps = {
#     "platformName": "android",
#     "platformVersion": "4.4.2",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.jd.app.reader",
#     "appActivity": "com.jingdong.app.reader.logo.JdLogoActivity",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True
#
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
# res = driver.find_elements_by_class_name('android.widget.TextView')
# print(len(res))
#
# res[0].click()


# --------------------- 层级定位 ------------

# import time
# from appium import webdriver
#
# desired_caps = {
#     "platformName": "android",
#     "platformVersion": "4.4.2",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.jd.app.reader",
#     "appActivity": "com.jingdong.app.reader.logo.JdLogoActivity",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True
#
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.find_element_by_id("com.jd.app.reader:id/skip_tv").click()
# time.sleep(3)
#
# # 通过text定位
# driver.find_element_by_android_uiautomator('new UiSelector().text("书架")').click()
# time.sleep(2)
#
# # 通过 resourceId 定位
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.jd.app.reader:id/main_tab_bookcity_txt")').click()


# --------------------- 等待机制 -----------------

# import time
# from appium import webdriver
#
# desired_caps = {
#     "platformName": "android",
#     "platformVersion": "4.4.2",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.jd.app.reader",
#     "appActivity": "com.jingdong.app.reader.logo.JdLogoActivity",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True
#
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.find_element_by_id("com.jd.app.reader:id/skip_tv").click()
#
# def swipeUp(driver, t=500, n=1):
#     '''向上滑动屏幕'''
#     l = driver.get_window_size()
#     x1 = l['width'] * 0.5  # x坐标
#     y1 = l['height'] * 0.75  # 起始y坐标
#     y2 = l['height'] * 0.25  # 终点y坐标
#     for i in range(n):
#         driver.swipe(x1, y1, x1, y2, t)
#
#
# def swipeDown(driver, t=500, n=1):
#     '''向下滑动屏幕'''
#     l = driver.get_window_size()
#     x1 = l['width'] * 0.5  # x坐标
#     y1 = l['height'] * 0.25  # 起始y坐标
#     y2 = l['height'] * 0.75  # 终点y坐标
#     for i in range(n):
#         driver.swipe(x1, y1, x1, y2, t)
#
#
# def swipLeft(driver, t=500, n=1):
#     '''向左滑动屏幕'''
#     l = driver.get_window_size()
#     x1 = l['width'] * 0.75
#     y1 = l['height'] * 0.5
#     x2 = l['width'] * 0.25
#     for i in range(n):
#         driver.swipe(x1, y1, x2, y1, t)
#
#
# def swipRight(driver, t=500, n=1):
#     '''向右滑动屏幕'''
#     l = driver.get_window_size()
#     x1 = l['width'] * 0.25
#     y1 = l['height'] * 0.5
#     x2 = l['width'] * 0.75
#     for i in range(n):
#         driver.swipe(x1, y1, x2, y1, t)
#
#
#
# if __name__ == '__main__':
#     time.sleep(4)
#     swipLeft(driver, n=2)
#     time.sleep(4)
#     swipRight(driver, n=2)
#     time.sleep(4)
#     swipeUp(driver, n=2)
#     time.sleep(4)
#     swipeDown(driver, n=2)


# -------------------- 九宫格 ------------

# import time
# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
#
# desired_caps = {
#     "platformName": "android",
#     "platformVersion": "4.4.2",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.duome.locus",
#     "appActivity": "com.jiugongge.java.LoginActivity",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True
#
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# element = driver.find_element_by_id('com.duome.locus:id/mLocusPassWordView')
# print(element.size)  # {'height': 1141, 'width': 720}
#
#
#
# def get_coordinate(x, y):
#     """ 获取指定图标的width和hight，x, y表示你想选中的指定坐标x，y轴 """
#     return element.size['width'] / 6 * x, element.size['height'] / 9 * y
#
#
# # 第1个图标
# width, height = get_coordinate(1, 3)
# TouchAction(driver).press(None, x=width, y=height).perform()
# # 第2个图标
# time.sleep(1)
# width, height = get_coordinate(3, 3)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # 第3个图标
# time.sleep(1)
# width, height = get_coordinate(5, 3)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # 第4个图标
# time.sleep(1)
# width, height = get_coordinate(1, 5)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # 第5个图标
# time.sleep(1)
# width, height = get_coordinate(3, 5)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # 第6个图标
# time.sleep(1)
# width, height = get_coordinate(5, 5)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # 第7个图标
# time.sleep(1)
# width, height = get_coordinate(1, 7)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # 第8个图标
# time.sleep(1)
# width, height = get_coordinate(3, 7)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # 第9个图标
# time.sleep(1)
# width, height = get_coordinate(5, 7)
# TouchAction(driver).press(None, x=width, y=height).perform()


# import time
# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
#
# desired_caps = {
#     "platformName": "android",
#     "platformVersion": "4.4.2",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.duome.locus",
#     "appActivity": "com.jiugongge.java.LoginActivity",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True
#
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# element = driver.find_element_by_id('com.duome.locus:id/mLocusPassWordView')
# print(element.size)  # {'height': 1141, 'width': 720}
#
#
# def get_coordinate(x, y):
#     """ 获取指定图标的width和height，x, y表示你想选中的指定坐标x，y轴 """
#     return element.size['width'] / 6 * x, element.size['height'] / 9 * y
#
# for y in range(3, 8, 2):   # 3 5 7
#     for x in range(1, 6, 2):  # 1 3 5
#         width, height = get_coordinate(x, y)
#         driver.tap([(width, height)], 500)


# def gen():
#     for y in range(3, 8, 2):
#         for x in range(1, 6, 2):
#             yield get_coordinate(x, y)
#
#
# def main():
#     # 首先拿到生成器
#     generator = gen()
#     # 先拿到第一个点
#     width, height = next(generator)
#     # 有了第一个点的width和height，就按住不松手
#     obj = TouchAction(driver)
#     obj.press(None, width, height).wait(500).perform()
#     # 然后循环移动到后续的每个点
#     for width, height in generator:
#         obj.move_to(None, width, height).wait(500).perform()
#     # 最后再释放即可
#     obj.release()
#
#
# if __name__ == '__main__':
#     main()

# ---------------------- 多单触控 --------------------

# import time
# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction
#
# desired_caps = {
#     "platformName": "android",
#     "platformVersion": "4.4.2",
#     "deviceName": "127.0.0.1:62001",
#     "appPackage": "com.baidu.BaiduMap",
#     "appActivity": "com.baidu.baidumaps.WelcomeScreen",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True
#
# }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(10)
# # 跳过一些基础的设置和提示
# driver.find_element_by_id('com.baidu.BaiduMap:id/ok_btn').click()
# driver.find_element_by_id('com.baidu.BaiduMap:id/btn_enter_map').click()
# driver.find_element_by_id('com.baidu.BaiduMap:id/guide_close').click()
# time.sleep(5)
#
# def get_window_size():
#     """ 获取窗口大小 """
#     size_dict = driver.get_window_size()
#     return size_dict.get('width'), size_dict.get('height')
#
#
# def shrink():
#     """ 缩小 """
#     x, y = get_window_size()
#     action1 = action2 = TouchAction(driver)
#     mu_obj = MultiAction(driver)
#     action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.4, y=y * 0.45).wait(1000).release()
#     action2.press(x=x * 0.4, y=y * 0.8).wait(1000).move_to(x=x * 0.4, y=y * 0.7).wait(1000).release()
#     mu_obj.add(action1, action2)
#     mu_obj.perform()
#
#
# def magnify():
#     """ 放大 """
#     x, y = get_window_size()
#     action1 = action2 = TouchAction(driver)
#     mu_obj = MultiAction(driver)
#     action1.press(x=x * 0.4, y=y * 0.45).wait(1000).move_to(x=x * 0.4, y=y * 0.4).wait(1000).release()
#     action2.press(x=x * 0.4, y=y * 0.7).wait(1000).move_to(x=x * 0.4, y=y * 0.8).wait(1000).release()
#     mu_obj.add(action1, action2)
#     mu_obj.perform()
#
#
# if __name__ == '__main__':
#     shrink()
#     time.sleep(5)
#     magnify()


# ---------------------- 读取 ini 文件 ------------------


# from configparser import ConfigParser
#
# obj = ConfigParser()
#
# print(obj.sections())  # []
# file_path = './my.ini'
# obj.read(file_path)
# print(obj.sections())
#
# # 创建一个字段
# obj.add_section('wang')
# obj.add_section('zhang')
#
# # 删除一个字段
# obj.remove_section('wang')
#
# # 删除一个option
#
# obj.remove_option('mysql', 'user')
#
# # 为指定的字段 mysql 添加 option， 注意，指定字段必须存在
# obj.set('mysql', 'user1', '234')
#
# # 最后，别忘了，将最新修改的结果更新到文件中
# obj.write(open(file_path, 'w'))


# from configparser import ConfigParser
#
# obj = ConfigParser()
#
# # 2. 操作文件
#
# file_path = './my.ini'
# obj.read(file_path)
# # print(obj.sections())  # ['client', 'mysql']
# # 判断字段是否存在
# print('client' in obj)  # True
# print('client' not in obj)  # False
#
# # 取值
# print(obj['DEFAULT']['default-character-set'])  # utf8
# print(obj['mysql'])  # <Section: mysql>
# for key in obj['mysql']:
#     print(key)
#
# print(obj['mysql']['user'])  # root
#
# # 返回mysql字段下所有的键值对
# print(obj.items('mysql'))  # [('default-character-set', 'utf8'), ('user', 'root'), ('password', '123')]
#
# # 同for循环，取 mysql字段下所有的键
# print(obj.options('mysql'))  # ['user', 'password', 'default-character-set']
#
# # get方法取嵌套的值
# print(obj.get('mysql', 'user'))  # root

# 1. 创建文件
# '''
# [client]
# default-character-set=utf8
#
# [mysql]
# user=root
# password=123
# '''
#
# obj['default'] = {'default-character-set': 'utf8'}
# obj['client'] = {'default-character-set': 'utf8'}
# obj['mysql'] = {'user': 'root', 'password': 123}
#
# with open('./my.ini', 'w') as f:
#     obj.write(f)


# 操作文件


# ----------- yaml -----------

# import yaml

# d = {
#     "client": {"default-character-set": "utf8"},
#     "mysql": {"user": 'root', "password": 123},
#     "custom": {
#         "user1": {"user": "zhangkai", "pwd": 666},
#         "user2": {"user": "zhangkai", "pwd": 999},
#     }
# }
#
# print(yaml.dump(d))
# with open('./my.yaml', 'w', encoding='utf-8') as fw:
#     yaml.dump(d, fw)


# file_path = './my.yaml'
# with open(file_path, 'r', encoding='utf-8') as fr:
#     data = yaml.load(fr, yaml.FullLoader)
#
# data['mysql']['user'] = 'new_root'
#
#
#
# with open(file_path, 'w', encoding='utf-8') as fw:
#     yaml.dump(data, fw)


# ---------------- 解决验证码 -------------------

'''
pip install pytesseract   # 识别规范字体还行
pip install baidu-aip
'''


# import pytesseract
# from selenium import webdriver
# from PIL import Image
# from aip import AipOcr
# driver = webdriver.Chrome()
# driver.get('https://pythonav.com/login/')
# driver.maximize_window()
# file_path = './code.png'
#
#
# def initial():
#     """ 初始化连接 """
#     APP_ID = '16611607'
#     API_KEY = 'wAIXfXOUS8ztLa4FrK3rZex1'
#     SECRET_KEY = '3b8nvjSGUZq0LPC18VVAizKYRBbny6Mq'
#     return AipOcr(APP_ID, API_KEY, SECRET_KEY)
#
# def get_file_content(filePath):
#     """ 读取图片 """
#     with open(filePath, 'rb') as f:
#         return f.read()
#
#
# def save_img():
#     """ 剪切图片 """
#     element = driver.find_element_by_id('image_code')
#     # print(element.location)  # {'x': 1006, 'y': 301}
#     # print(element.size)  # {'height': 30, 'width': 120}
#     driver.save_screenshot(file_path)
#     left = element.location['x']
#     top = element.location['y']
#     right = element.size['width'] + left
#     height = element.size['height'] + top
#     img = Image.open(file_path)
#     img = img.crop((left, top, right, height))
#     img.save(file_path)
#
#
# def discern():
#     """ 识别验证码 """
#     client = initial()
#     image = get_file_content(file_path)
#     res = client.basicGeneral(image)
#     print(res)
#
#
# try:
#
#     save_img()
#     discern()
#
#
# finally:
#     driver.quit()


# import sys
# import time
# import datetime
# import requests
# import unittest
# from HTMLTestRunner import HTMLTestRunner
# from threading import Thread
# from concurrent.futures import ThreadPoolExecutor
# from multiprocessing import cpu_count
#
#
# class myTestCase(unittest.TestCase):
#
#     def test_01(self):
#         res = requests.get('https://www.baidu.com/')
#         self.assertEqual(res.status_code, 200)
#
#     def test_02(self):
#         res = requests.get('https://www.baidu.com/')
#         self.assertEqual(res.status_code, 201)
#
#     def test_03(self):
#         res = requests.get('https://www.baidu.com/')
#         self.assertEqual(res.status_code, 210)
#
#     def test_04(self):
#         res = requests.get('https://www.baidu.com/')
#         self.assertEqual(res.status_code, '200')
#
#
#
# def get_suite():
#     """ 制作suite """
#     suite = unittest.makeSuite(myTestCase)
#     return suite
#
# def worker(case):
#     """ 执行case方法, 根据需要放开或注释 """
#     print(case.__dict__['_testMethodName'])
#     fp1 = open('./{}.html'.format(case.__dict__['_testMethodName']), 'wb')
#     fp2 = open('./report.html', 'ab')
#     HTMLTestRunner(stream=fp1, title='{}执行结果报告'.format(case.__dict__['_testMethodName'])).run(case)
#     HTMLTestRunner(stream=fp2, title='{}执行结果报告'.format(case.__dict__['_testMethodName'])).run(case)
#
#
# def thread_pool():
#     """ 线程池 """
#     suite = get_suite()
#     countTestCases = suite.countTestCases()
#     t = ThreadPoolExecutor(countTestCases) if countTestCases <= cpu_count() * 5 else ThreadPoolExecutor(
#         cpu_count() * 5)
#     for case in suite:
#         t.submit(worker, case)
#     t.shutdown()
#
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     thread_pool()


# import subprocess


# import yaml
#
# with open('./my.yaml', 'w') as f:
#     f.truncate()
# f.close()


# from appium import webdriver
#
# desired_caps = {
#     "platformName": "android",
#     "platformVersion": "4.4.2",
#     "deviceName": "127.0.0.1:62025",
#     "appPackage": "com.jd.app.reader",
#     "appActivity": "com.jingdong.app.reader.logo.JdLogoActivity"
# }
#
# driver = webdriver.Remote('http://127.0.0.1:4700/wd/hub', desired_caps)
# print(driver.get_window_size())  # {'width': 720, 'height': 1280}
#
#
#
# driver.quit()


# import cv2
# import numpy as np
# from PIL import ImageGrab
# from threading import Thread
# import ffmpy3
#
# a = False
#
#
# def f1():
#     ffmpy3.FFmpeg(inputs={'./test.mp4': None}, outputs={'test1.mp4': None}).run()
#
#
# def f2():
#     p = ImageGrab.grab()
#     width, height = p.size
#     fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#
#     video = cv2.VideoWriter('./test.mp4', fourcc, 8, (width, height), True)
#     while 1:
#         img = ImageGrab.grab()
#         img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#         video.write(img_bgr)
#         if a:
#             break
#     video.release()
#     f1()
#
#
# def f3():
#     global a
#     import time
#     time.sleep(3)
#     a = True


# if __name__ == '__main__':


# def f1():
#     yield 1
#     yield 2
#     yield 3
#
# def handle():
#     return f1()
# for i in handle():
#     print(i)


# import time
# from selenium import webdriver  # 驱动浏览器
#
# browser = webdriver.Chrome()
# browser.get('https://www.cnblogs.com/neeo')
# browser.execute_script('alert("xxoo")')
# print(12312132)
# time.sleep(3)
# browser.quit()
# Thread(target=f3).start()
# f2()
# ff = ffmpy3.FFmpeg(
#     inputs={'./test.mp4': None},
#     outputs={'./test1.mp4': '-vcode h264'}
# )
# print(ff.cmd)  # ffmpeg -i ./test.mp4 -vcode h264 ./test1.mp4

# import hashlib
# import time
# print(time.time())
# print(hashlib.md5("{}".format(time.time()).encode()).hexdigest())
# import time
# def bar():
#     foo()
#     global a
#     from selenium import webdriver  # 驱动浏览器
#     from selenium.webdriver import ActionChains  # 鼠标的相关操作，比如滑动验证
#     from selenium.webdriver.common.by import By  # 选择器，以什么方式选择标签元素
#     from selenium.webdriver.common.keys import Keys  # 键盘相关
#     from selenium.webdriver.support import expected_conditions as EC  # 各种判断，一般跟等待事件连用，比如说等待某个元素加载出来
#     from selenium.webdriver.support.wait import WebDriverWait  # 等待事件，可以与EC连用
#
#     browser = webdriver.Chrome()
#     wait = WebDriverWait(browser, 10)
#     browser.get('https://www.baidu.com')
#     browser.maximize_window()  # 窗口最大化
#     print(browser.current_url)  # 获取当前页URL
#     print(browser.title)  # 获取页面的title
#     print(browser.name)  # 获取driver对象：chrome
#     print(browser.current_window_handle)  # 获取当前窗口
#     print(browser.get_cookies())  # 获取cookies
#     print(browser.page_source)  # 获取当前页面内容
#     browser.close()  # 关闭当前窗口
#     browser.quit()  # 退出浏览器驱动，关闭所有关联窗口
#
#
#
#     a = True
# bar()

# import time
# from threading import Thread


# class A(object):
#
#     status = False
#     def p1(self):
#         print(3333333333333)
#         # t1 = Thread(target=self.p1)
#         t2 = Thread(target=self.p2)
#         # t1.start()
#         t2.start()
#         time.sleep(3)
#         self.status = True
#         print(33333333333)
#
#     def p2(self):
#         print(1111111111111)
#         while 1:
#             print(2222222222222)
#             time.sleep(1)
#             if self.status:
#                 break
# A().p1()

# class Base(object):
#
#     def foo(self): pass
#
#     def bar(self): pass
#
#
# class Derived(Base):
#
#     def foo(self): pass
#
#
# case1 = Derived().foo()
# case2 = Derived().bar()
#
# # 要考虑到面向对象的继承关系
# case3 = Base().foo()
# case4 = Base().bar()


# from __future__ import print_function
#
# import resources
#
# class A(object):
#     def __init__(self):
#         self.a = 'string'
#         self.b = 10
#         self.c = True
#
#
# class B(object):
#     __slots__ = ['a', 'b', 'c']
#     def __init__(self):
#         self.a = 'string'
#         self.b = 10
#         self.c = True
#
#
# def test(cls):
#     mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
#     l = []
#     for i in range(500000):
#         l.append(cls())
#     mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
#     del l
#     print('Class: {}:\n'.format(getattr(cls, '__name__')))
#     print('Initial RAM usage: {:14,}'.format(mem_init))
#     print('  Final RAM usage: {:14,}'.format(mem_final))
#     print('-' * 20)
#
#
# if __name__ == '__main__':
#     import sys
#     test(globals()[sys.argv[1].upper()])


# '''
# pip install memory_profiler
# pip install -i https://pypi.doubanio.com/simple/ memory_profiler
# https://pypi.org/project/memory-profiler/
# '''
#
# from memory_profiler import profile
#
#
# class A(object):  # 没有定义__slots__属性
#     # __slots__ = ("x",)
#
#     def __init__(self, x):
#         self.x = x
#
#
# @profile
# def main():
#     f = [A(523825) for i in range(1000000)]
#
#
# if __name__ == '__main__':
#     main()


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()


p = Stack()
p.push('a')
p.pop()

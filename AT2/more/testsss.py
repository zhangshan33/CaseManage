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


# --------------- ��ȡ��Ļ�Ĵ�С ---------------
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


# --------------------- ͨ��id��λ -------------------

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
# # ���������ҳ���
# driver.find_element_by_id('com.jd.app.reader:id/skip_tv').click()
# time.sleep(1)
# # ��������������
# driver.find_element_by_id('com.jd.app.reader:id/mSearchLayout').send_keys()
# time.sleep(1)
# # ���µ�����ҳ������ֵ
# driver.find_element_by_id('com.jd.app.reader:id/mSearchKeyInput').send_keys('�Ϲž���')
# time.sleep(1)
# # ����ֵ���Ϳ��Ե��������ť��������
# driver.find_element_by_id('com.jd.app.reader:id/mSearchBtn').click()

# --------------------- ͨ��class��λ -------------------

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


# --------------------- �㼶��λ ------------

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
# # ͨ��text��λ
# driver.find_element_by_android_uiautomator('new UiSelector().text("���")').click()
# time.sleep(2)
#
# # ͨ�� resourceId ��λ
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.jd.app.reader:id/main_tab_bookcity_txt")').click()


# --------------------- �ȴ����� -----------------

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
#     '''���ϻ�����Ļ'''
#     l = driver.get_window_size()
#     x1 = l['width'] * 0.5  # x����
#     y1 = l['height'] * 0.75  # ��ʼy����
#     y2 = l['height'] * 0.25  # �յ�y����
#     for i in range(n):
#         driver.swipe(x1, y1, x1, y2, t)
#
#
# def swipeDown(driver, t=500, n=1):
#     '''���»�����Ļ'''
#     l = driver.get_window_size()
#     x1 = l['width'] * 0.5  # x����
#     y1 = l['height'] * 0.25  # ��ʼy����
#     y2 = l['height'] * 0.75  # �յ�y����
#     for i in range(n):
#         driver.swipe(x1, y1, x1, y2, t)
#
#
# def swipLeft(driver, t=500, n=1):
#     '''���󻬶���Ļ'''
#     l = driver.get_window_size()
#     x1 = l['width'] * 0.75
#     y1 = l['height'] * 0.5
#     x2 = l['width'] * 0.25
#     for i in range(n):
#         driver.swipe(x1, y1, x2, y1, t)
#
#
# def swipRight(driver, t=500, n=1):
#     '''���һ�����Ļ'''
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


# -------------------- �Ź��� ------------

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
#     """ ��ȡָ��ͼ���width��hight��x, y��ʾ����ѡ�е�ָ������x��y�� """
#     return element.size['width'] / 6 * x, element.size['height'] / 9 * y
#
#
# # ��1��ͼ��
# width, height = get_coordinate(1, 3)
# TouchAction(driver).press(None, x=width, y=height).perform()
# # ��2��ͼ��
# time.sleep(1)
# width, height = get_coordinate(3, 3)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # ��3��ͼ��
# time.sleep(1)
# width, height = get_coordinate(5, 3)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # ��4��ͼ��
# time.sleep(1)
# width, height = get_coordinate(1, 5)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # ��5��ͼ��
# time.sleep(1)
# width, height = get_coordinate(3, 5)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # ��6��ͼ��
# time.sleep(1)
# width, height = get_coordinate(5, 5)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # ��7��ͼ��
# time.sleep(1)
# width, height = get_coordinate(1, 7)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # ��8��ͼ��
# time.sleep(1)
# width, height = get_coordinate(3, 7)
# TouchAction(driver).press(None, x=width, y=height).perform()
#
# # ��9��ͼ��
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
#     """ ��ȡָ��ͼ���width��height��x, y��ʾ����ѡ�е�ָ������x��y�� """
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
#     # �����õ�������
#     generator = gen()
#     # ���õ���һ����
#     width, height = next(generator)
#     # ���˵�һ�����width��height���Ͱ�ס������
#     obj = TouchAction(driver)
#     obj.press(None, width, height).wait(500).perform()
#     # Ȼ��ѭ���ƶ���������ÿ����
#     for width, height in generator:
#         obj.move_to(None, width, height).wait(500).perform()
#     # ������ͷż���
#     obj.release()
#
#
# if __name__ == '__main__':
#     main()

# ---------------------- �൥���� --------------------

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
# # ����һЩ���������ú���ʾ
# driver.find_element_by_id('com.baidu.BaiduMap:id/ok_btn').click()
# driver.find_element_by_id('com.baidu.BaiduMap:id/btn_enter_map').click()
# driver.find_element_by_id('com.baidu.BaiduMap:id/guide_close').click()
# time.sleep(5)
#
# def get_window_size():
#     """ ��ȡ���ڴ�С """
#     size_dict = driver.get_window_size()
#     return size_dict.get('width'), size_dict.get('height')
#
#
# def shrink():
#     """ ��С """
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
#     """ �Ŵ� """
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


# ---------------------- ��ȡ ini �ļ� ------------------


# from configparser import ConfigParser
#
# obj = ConfigParser()
#
# print(obj.sections())  # []
# file_path = './my.ini'
# obj.read(file_path)
# print(obj.sections())
#
# # ����һ���ֶ�
# obj.add_section('wang')
# obj.add_section('zhang')
#
# # ɾ��һ���ֶ�
# obj.remove_section('wang')
#
# # ɾ��һ��option
#
# obj.remove_option('mysql', 'user')
#
# # Ϊָ�����ֶ� mysql ��� option�� ע�⣬ָ���ֶα������
# obj.set('mysql', 'user1', '234')
#
# # ��󣬱����ˣ��������޸ĵĽ�����µ��ļ���
# obj.write(open(file_path, 'w'))


# from configparser import ConfigParser
#
# obj = ConfigParser()
#
# # 2. �����ļ�
#
# file_path = './my.ini'
# obj.read(file_path)
# # print(obj.sections())  # ['client', 'mysql']
# # �ж��ֶ��Ƿ����
# print('client' in obj)  # True
# print('client' not in obj)  # False
#
# # ȡֵ
# print(obj['DEFAULT']['default-character-set'])  # utf8
# print(obj['mysql'])  # <Section: mysql>
# for key in obj['mysql']:
#     print(key)
#
# print(obj['mysql']['user'])  # root
#
# # ����mysql�ֶ������еļ�ֵ��
# print(obj.items('mysql'))  # [('default-character-set', 'utf8'), ('user', 'root'), ('password', '123')]
#
# # ͬforѭ����ȡ mysql�ֶ������еļ�
# print(obj.options('mysql'))  # ['user', 'password', 'default-character-set']
#
# # get����ȡǶ�׵�ֵ
# print(obj.get('mysql', 'user'))  # root

# 1. �����ļ�
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


# �����ļ�


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


# ---------------- �����֤�� -------------------

'''
pip install pytesseract   # ʶ��淶���廹��
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
#     """ ��ʼ������ """
#     APP_ID = '16611607'
#     API_KEY = 'wAIXfXOUS8ztLa4FrK3rZex1'
#     SECRET_KEY = '3b8nvjSGUZq0LPC18VVAizKYRBbny6Mq'
#     return AipOcr(APP_ID, API_KEY, SECRET_KEY)
#
# def get_file_content(filePath):
#     """ ��ȡͼƬ """
#     with open(filePath, 'rb') as f:
#         return f.read()
#
#
# def save_img():
#     """ ����ͼƬ """
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
#     """ ʶ����֤�� """
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
#     """ ����suite """
#     suite = unittest.makeSuite(myTestCase)
#     return suite
#
# def worker(case):
#     """ ִ��case����, ������Ҫ�ſ���ע�� """
#     print(case.__dict__['_testMethodName'])
#     fp1 = open('./{}.html'.format(case.__dict__['_testMethodName']), 'wb')
#     fp2 = open('./report.html', 'ab')
#     HTMLTestRunner(stream=fp1, title='{}ִ�н������'.format(case.__dict__['_testMethodName'])).run(case)
#     HTMLTestRunner(stream=fp2, title='{}ִ�н������'.format(case.__dict__['_testMethodName'])).run(case)
#
#
# def thread_pool():
#     """ �̳߳� """
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
# from selenium import webdriver  # ���������
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
#     from selenium import webdriver  # ���������
#     from selenium.webdriver import ActionChains  # ������ز��������绬����֤
#     from selenium.webdriver.common.by import By  # ѡ��������ʲô��ʽѡ���ǩԪ��
#     from selenium.webdriver.common.keys import Keys  # �������
#     from selenium.webdriver.support import expected_conditions as EC  # �����жϣ�һ����ȴ��¼����ã�����˵�ȴ�ĳ��Ԫ�ؼ��س���
#     from selenium.webdriver.support.wait import WebDriverWait  # �ȴ��¼���������EC����
#
#     browser = webdriver.Chrome()
#     wait = WebDriverWait(browser, 10)
#     browser.get('https://www.baidu.com')
#     browser.maximize_window()  # �������
#     print(browser.current_url)  # ��ȡ��ǰҳURL
#     print(browser.title)  # ��ȡҳ���title
#     print(browser.name)  # ��ȡdriver����chrome
#     print(browser.current_window_handle)  # ��ȡ��ǰ����
#     print(browser.get_cookies())  # ��ȡcookies
#     print(browser.page_source)  # ��ȡ��ǰҳ������
#     browser.close()  # �رյ�ǰ����
#     browser.quit()  # �˳�������������ر����й�������
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
# # Ҫ���ǵ��������ļ̳й�ϵ
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
# class A(object):  # û�ж���__slots__����
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

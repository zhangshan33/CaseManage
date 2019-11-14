# -*- coding: utf-8 -*-
# __author__ = "maple"


import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login(user, pwd):
    """ 登录163邮箱 """
    # 由于可以扫码登录，而我们选择用户名和密码登录，所以，要点击 密码登录
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, 'switchAccountLogin'))).click()
    # 进入iframe，因为有多个iframe，所以获取的是数组，在分析页面后，数组0索引的iframe是登陆的iframe
    time.sleep(3)
    iframe = driver.find_elements_by_tag_name('iframe')
    # print(iframe)
    '''
    [
        <selenium.webdriver.remote.webelement.WebElement (session="3f92dbd96e72746e7d27d64e6b412318", element="0.855888743369456-2")>, 
        <selenium.webdriver.remote.webelement.WebElement (session="3f92dbd96e72746e7d27d64e6b412318", element="0.855888743369456-3")>, 
        <selenium.webdriver.remote.webelement.WebElement (session="3f92dbd96e72746e7d27d64e6b412318", element="0.855888743369456-4")>, 
        <selenium.webdriver.remote.webelement.WebElement (session="3f92dbd96e72746e7d27d64e6b412318", element="0.855888743369456-5")>
    ]
    '''
    driver.switch_to.frame(iframe[0])

    # 获取用户名和密码标签，并输入对应的值
    time.sleep(1)
    driver.find_element_by_class_name('dlemail').send_keys(user)
    time.sleep(2)
    driver.find_element_by_class_name('dlpwd').send_keys(pwd)
    time.sleep(2)
    driver.find_element_by_id('dologin').click()


def send_mail():
    """ 发送163邮件，需要传递163的用户名和密码,收件人和内容 """

    try:
        # 第1步，执行登陆
        login(user, pwd)

        # 第2步，点击写信按钮
        wait.until(EC.presence_of_element_located((By.ID, '_mail_component_24_24'))).click()
        # driver.find_element_by_id('_mail_component_24_24').click()

        # 第3步，获取收件人，主题，内容框标签，写入内容
        time.sleep(1)
        # 3.1 填写收件人
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'nui-editableAddr-ipt'))).send_keys(addr)  # 收件人
        time.sleep(2)
        # 3.2 填写主题
        title = driver.find_elements_by_class_name('nui-ipt-input')
        # print(11111, title)
        title[2].send_keys(theme)  # 主题
        # title.send_keys(theme)  # 主题

        # 3.3 进入content所在iframe，填写内容
        time.sleep(1)
        content_iframe = driver.find_element_by_class_name('APP-editor-iframe')
        driver.switch_to.frame(content_iframe)
        # 虽然nui-scroll这个类名在整个网页中有多个，但是这个iframe中只有一个，所以我们直接send_keys就行
        nui_scroll = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'nui-scroll')))
        # print(22222222, nui_scroll)  # <selenium.webdriver.remote.webelement.WebElement (session="106a6f5778c14568827014435ddcfcd9", element="0.07847410617283446-1")>
        nui_scroll.send_keys(content)
        # 第4步，因为发送按钮不在此时的iframe中，所以要先退出iframe，才能点击发送按钮
        # 4.1 退出iframe
        time.sleep(1)
        driver.switch_to.default_content()
        # 4.2 点击发送按钮
        time.sleep(1)
        # 这个发送按钮的类名有多个，最好for循环一下，因为有坑，发送按钮是第3个，前面还有两个空标签，但是前端检查中看不到
        driver.find_elements_by_class_name('nui-btn-text')[2].click()

    finally:
        # 关闭浏览器
        time.sleep(3)
        driver.quit()
        # 截止2019-6-11，代码无误


if __name__ == '__main__':

    from getpass import getpass
    user = input("邮箱: ").strip()  # 填写你的163账号
    pwd = getpass('密码: ')  # 填写你的163密码
    # 获取driver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    # driver.maximize_window()
    # 发请求
    driver.get('https://mail.163.com/')

    addr = "1206180814@qq.com"  # 收件人
    theme = '我是你爸爸'  # 主题
    content = '天不生我李淳罡，剑道万古如长夜 ————\n{}'.format(datetime.datetime.now())  # 发送内容
    send_mail()
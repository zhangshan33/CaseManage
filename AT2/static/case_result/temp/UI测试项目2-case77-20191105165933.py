from selenium import webdriver   # 驱动浏览器
from selenium.webdriver import ActionChains   # 鼠标的相关操作，比如滑动验证
from selenium.webdriver.common.by import By   # 选择器，以什么方式选择标签元素
from selenium.webdriver.common.keys import Keys   # 键盘相关
from selenium.webdriver.support import expected_conditions as EC  # 各种判断，一般跟等待事件连用，比如说等待某个元素加载出来
from selenium.webdriver.support.wait import WebDriverWait  # 等待事件，可以与EC连用

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
browser.get('https://www.baidu.com')
browser.maximize_window()  # 窗口最大化
print(browser.current_url)   # 获取当前页URL
print(browser.title)   # 获取页面的title
print(browser.name)  # 获取driver对象：chrome
browser.quit()
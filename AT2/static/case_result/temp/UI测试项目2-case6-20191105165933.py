import time
from selenium import webdriver  # 驱动浏览器
browser = webdriver.Chrome()
browser.get('https://blog.csdn.net/weixin_33595571/article/details/84206196')
browser.execute_script('alert("xxoo")')
print(12312132)
time.sleep(5)
browser.quit()
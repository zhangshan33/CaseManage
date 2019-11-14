import time
from selenium import webdriver  # 驱动浏览器
browser = webdriver.Chrome()
browser.get('https://blog.csdn.net/NCS123456/article/details/84769146')
browser.execute_script('alert("xxoo")')
print(12312132)
time.sleep(3)
browser.quit()
from appium import webdriver

desired_caps = {
    "platformName": "android",
    "platformVersion": "4.4.2",
    "deviceName": "127.0.0.1:52001",
    "appPackage": "com.jd.app.reader",
    "appActivity": "com.jingdong.app.reader.logo.JdLogoActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4700/wd/hub', desired_caps)
print(driver.get_window_size())  # {'width': 720, 'height': 1280}
print(driver.get_window_size()['width'])  # 720
print(driver.get_window_size()['height'])  # 1280
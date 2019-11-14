#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "张开"
# Date: 2019/10/12

import os
import json
from subprocess import PIPE
from subprocess import Popen
from subprocess import STDOUT
from util import tools as public_tools
from AT2.settings import BASE_DIR, EXECUTE_COMMAND

class ExecuteDevices(public_tools.ExecuteCommand, public_tools.TextIO):
    """ 处理devices和执行appium脚本 """

    def get_devices(self):
        """ 获取devices """
        return self._filter_devices()

    def _filter_devices(self):
        """ 过滤可用的 devices """
        # 执行命令
        command_msg = 'adb devices'
        result = self.execute_command(command_msg)
        l = []
        for i in result:
            temp = json.loads(i)['result_msg'].strip()
            if temp:
                if 'List' not in temp:
                    l.append(temp)
        return l

    def get_execute_handle(self, data_msg):
        """ 获取终端命令的执行结果 """
        # 过滤敏感命令
        print(1111111, data_msg)
        if hasattr(self, '_{}'.format(data_msg['type_msg'])):
            return getattr(self, '_{}'.format(data_msg['type_msg']))(data_msg)
        else:
            return self.dumps({"result_msg": '无法执行的命令类型：{}'.format(data_msg['type_msg'])})

    def _appium(self, data_msg):
        """ 执行appium代码 """
        # 过滤敏感命令
        if self.filter_command(data_msg['send_msg']):
            return self.dumps({"result_msg": '含有敏感命令'})
        else:
            # 将appium脚本写入到一个临时文件中
            self.temp_file_path = os.path.join(BASE_DIR, 'apm', 'util', 'temp.py')
            self.write_file(self.temp_file_path, data_msg['send_msg'], mode='w')
            # 使用 sbuprocess 执行终端命令
            py1 = 'python'
            command_msg = '{} {}'.format(py1, self.temp_file_path)

            # print(111111111111111111111, command_msg)
            return self.execute_command(command_msg)

    def _cmd(self, data_msg):
        """ 执行cmd命令 """
        # 过滤敏感命令
        if self.filter_command(data_msg['send_msg']):
            return self.dumps({"result_msg": '含有敏感命令'})
        else:
            # 执行终端命令
            command_msg = data_msg['send_msg']
            return self.execute_command(command_msg)


if __name__ == '__main__':
    obj = ExecuteDevices()
    res = obj.get_execute_handle({'send_msg': 'from appium import webdriver\n\ndesired_caps = {\n    "platformName": "android",\n    "platformVersion": "4.4.2",\n    "deviceName": "127.0.0.1:62025",\n    "appPackage": "com.jd.app.reader",\n    "appActivity": "com.jingdong.app.reader.logo.JdLogoActivity"\n}\n\ndriver = webdriver.Remote(\'http://127.0.0.1:4700/wd/hub\', desired_caps)\nprint(driver.get_window_size())  # {\'width\': 720, \'height\': 1280}\nprint(driver.get_window_size()[\'width\'])  # 720\nprint(driver.get_window_size()[\'height\'])  # 1280', 'type_msg': 'appium'})
    print(res)
    for i in res:
        print(i)

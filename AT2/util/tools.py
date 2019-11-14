#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "张开"
# Date: 2019/10/12

import os
import json
from subprocess import PIPE
from subprocess import Popen
from subprocess import STDOUT
from ffmpy3 import FFmpeg
from AT2 import settings


class TextIO(object):
    """ 文件处理 """

    def read_file(self, file_path, mode='r'):
        """ 读文件 """
        if mode == "rb":
            with open(file_path, mode) as f1:
                return f1.read()
        else:
            with open(file_path, mode, encoding='utf-8') as f2:
                return f2.read()

    def write_file(self, file_path, file_content, mode='w'):
        """ 写文件 """
        if mode == 'wb':
            with open(file_path, mode) as f1:
                f1.write(file_content)
        else:
            with open(file_path, mode, encoding='utf-8') as f2:
                f2.write(file_content)
    def remove_file(self, file_path):
        """ 删除文件 """
        if os.path.isfile(file_path):
            os.remove(file_path)

    def dumps(self, data):
        """ 序列化字典 """
        return json.dumps(data)

    def loads(self, data):
        """ 反序列化 """
        return json.loads(data)

    def transcoding_video(self, input_file, output_file):
        """ 视频转码，mpeg4转为h264"""
        # print(44444444444444, output_file)
        if os.path.isfile(output_file):
            # 把原来的视频删掉，不然后续FFmpeg转码时，会报 File 'M:\demo\AT2\media\ui\c6a54e8c962fffe261a21621be455512.mp4' already exists. Overwrite ? [y/N] Not overwriting - exiting
            self.remove_file(output_file)
        ff = FFmpeg(
            inputs={input_file: None},
            outputs={output_file: None}
        )
        # print(111111111111111111111, ff.cmd)
        ff.run()


class ExecuteCommand(object):
    """ 执行命令相关 """

    def execute_command(self, command_content):
        """ 执行命令"""
        execute_result = Popen(command_content, shell=True, stderr=STDOUT, stdout=PIPE).stdout
        for i in execute_result:
            print(1111111111, i)
            yield json.dumps({"result_msg": i.decode('gbk')})

    def filter_command(self, command):
        """ 过滤敏感的命令 """
        for value in settings.SENSITIVITY_COMMAND:
            # print(111111111111111111111, value, command)
            if value.lower() in command.lower():
                return True








def check_choices(choice_fields, case_list, case_fields):
    """ 处理字段中的choise
    choice_fields: ui_models.UiCase.case_execute_pass_choices   # 元组
    case_list，记录列表
    case_fields：ui_models.UiCase.case_execute_pass
    """
    for item in choice_fields:  # 循环字段
        for case in case_list:
            if case.__dict__[case_fields.__dict__['field_name']] == item[0]:
                case.__dict__[case_fields.__dict__['field_name']] = item[1]


if __name__ == '__main__':
    # res = ExecuteCommand().get_execute_result('dir')
    # from collections import Generator,Iterator
    # print(res, type(res))
    # print(isinstance(res, Generator))
    pass
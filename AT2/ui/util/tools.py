#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "张开"
# Date: 2019/9/24

"""
ui app tools
"""
import os
import time
import hashlib
import json
import subprocess
import shutil
import zipfile
import cv2
import numpy as np
from subprocess import STDOUT
from PIL import ImageGrab
from threading import Thread
from multiprocessing import Process
from util import tools as public_tools
from ui.models import UiCase

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_UI_UTIL_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_STATIC_CASE_RESULT = os.path.join(BASE_DIR, 'static', 'case_result')
S_AVI = os.path.join(BASE_DIR, 'static', 'selenium_avi')








class Execute(public_tools.TextIO):
    """ 执行在线编辑器的Python代码 """
    _status = False



    def execute_file(self, status=None, case_pk=None):
        # 前端传过来的是 字符串类型的 status
        self.case_pk = case_pk
        self._get_file_path()
        if int(status):  # 开启录制
            # 开启线程录制
            self.case_pk = case_pk
            Thread(target=self._write_avi).start()
            # Process(target=self._write_avi).start()
            # 运行文件，获取执行结果
            file_path = os.path.join(BASE_UI_UTIL_DIR, 'editor.py')
            result = subprocess.Popen('python {}'.format(file_path), shell=True, stdout=subprocess.PIPE, stderr=STDOUT)
            for i in result.stdout:
                # print(1111, i)
                yield json.dumps({'msg': i.decode()})

            # 文件执行完毕，结束录制
            self._status = True
        else:
            # 不开启录制
            file_path = os.path.join(BASE_UI_UTIL_DIR, 'editor.py')
            result = subprocess.Popen('python {}'.format(file_path), shell=True, stdout=subprocess.PIPE, stderr=STDOUT)
            for i in result.stdout:
                # print(1111, i)
                yield json.dumps({'msg': i.decode()})



    def _write_file(self, value):
        """ 写文件 """
        # 调用父类的写文件方法
        self.write_file(os.path.join(BASE_UI_UTIL_DIR, 'editor.py'), mode='w', file_content=value)

    def _write_avi(self):
        """ 录制selenium脚本执行过程 """
        # time.sleep(1)
        p = ImageGrab.grab()  # 获得当前屏幕信息
        width, height = p.size
        # print(width, height)
        # 录屏文件的编码格式
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        # 输出文件命名为test.avi,帧率为8，可以自己设置,注意，帧数会影响录制时长，设置为10左右是折中的办法
        video = cv2.VideoWriter(self.input_file, fourcc, 11, (width, height))
        while 1:
            img = ImageGrab.grab()
            img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            # 录制完整视频
            video.write(img_bgr)
            if self._status:
                break
        video.release()

        # 视频转码
        # print(111111111111111111111111)
        self.transcoding_video(self.input_file, self.output)

        # 删除临时文件 self.input_file
        # print(222222222222222, )
        self.remove_file(self.input_file)

        # 更新数据库
        # print(333333333333333333333)
        self._save_data()

    def _save_data(self):
        """ 更新数据库状态信息 """
        obj = UiCase.objects.filter(pk=self.case_pk).first()
        if not obj.case_media_report:
            obj.case_media_report = self.file_path
        obj.save()

    def _get_file_path(self):
        """ 配合录制视频，处理文件路径 """
        self.ui_case_obj = UiCase.objects.filter(pk=self.case_pk).first()

        if self.ui_case_obj.case_media_report:
            # 如果这个视频之前执行过，那么就取出来它的路径

            self.output = os.path.join(BASE_DIR, 'media', self.ui_case_obj.case_media_report)
            # print(1111111112222222222222, self.output)

        else:
            # print(333333333333333333333333, self.ui_case_obj.case_media_report)
            # 否则就生成一个文件路径和文件名
            md = hashlib.md5("{}".format(time.time()).encode()).hexdigest() + '.mp4'
            self.file_path = os.path.join('ui', md)
            self.output = os.path.join(BASE_DIR, 'media', self.file_path)
        self.input_file = os.path.join(BASE_DIR, 'media', 'temp.mp4')
        # print(3333333333333333, self.ui_case_obj.pk, self.ui_case_obj.case_name, self.ui_case_obj.case_media_report)




class MakePackage(object):
    """ 打包文件 """

    def __init__(self, case_list):
        self.case_list = case_list

    def create_zip(self):
        """ 创建压缩文件 """

        start_dir = os.path.join(BASE_STATIC_CASE_RESULT, 'temp')
        f = zipfile.ZipFile(os.path.join(BASE_STATIC_CASE_RESULT, 'temp.zip'), 'w', zipfile.ZIP_DEFLATED)
        for dir_path, dir_name, file_names in os.walk(start_dir):
            file_path = dir_path.replace(start_dir, '')
            file_path = file_path and file_path + os.sep or ''
            for file_name in file_names:
                f.write(os.path.join(dir_path, file_name), file_path + file_name)
        f.close()

    def get_zip_file(self):
        """ 创建打包文件 """
        self.temp_file_path = os.path.join(BASE_STATIC_CASE_RESULT, 'temp')
        # 创建目录
        if not os.path.isdir(self.temp_file_path):
            os.mkdir(self.temp_file_path)
        else:
            shutil.rmtree(self.temp_file_path)
            os.mkdir(self.temp_file_path)
        # 创建py文件
        for case in self.case_list:
            # print(case.case_name, case.case_vest_project.project_name)
            file_name = '{}-{}-{}.{}'.format(
                case.case_vest_project.project_name,
                case.case_name,
                time.strftime('%Y%m%d%H%M%S', time.localtime()),
                "py"
            )
            with open(file=os.path.join(self.temp_file_path, file_name), mode='w', encoding='utf-8') as f:
                f.write(case.case_code)
        # 创建压缩文件
        self.create_zip()





if __name__ == '__main__':
    # pass
    obj = Execute()
    obj.execute_file()

    # shutil.make_archive(
    #     base_name='ui_test_case',
    #     format='zip',
    #     base_dir=os.path.join(BASE_STATIC_CASE_RESULT, 'temp')
    # )

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "张开"
# Date: 2019/9/20

"""
<a href="127.0.0.1:8033/case/case_result_report/h" class="btn btn-success">导出HTML</a>
处理用例
    - 拿到用例对象
    - 进行测试
    - 修改相应的数据库状态
    - 生成测试报告
"""
import os
import time
import codecs
import queue
import pdfkit
import unittest
import requests
import HTMLTestRunner    # 基础的
import HTMLTestRunner2   # 带通过率图标的
from AT2.settings import BASE_DIR, WKHTMLTOIMAGE, WKHTMLTOPDF
from web import models
from django.http import FileResponse
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from multiprocessing import cpu_count
from web import models
from django.db.models import Count
from util import tools as public_tools
from io import BytesIO

class TesCase(unittest.TestCase):
    result = expect = None  # requests的返回结果和用例的预期值

    def runTest(self):
        """  """.format('测试用例')
        self.assertEqual(self.result, self.expect)


class ExecuteCase(public_tools.TextIO):
    """ 执行用例 """

    def __init__(self, case=None, case_list=[]):
        self.case = case
        self.case_list = case_list
        # if self.case:
        #     self.case_title = self.case.case_title
        # else:
        #     self.case_title = '用例报告'
        self.case_title = self.case.case_title if self.case else '批量用例执行报告'
        # if self.case:
        #     self.case_desc = self.case.case_desc
        # else:
        #     self.case_desc = '批量用例执行结果报告'
        self.case_desc = self.case.case_desc if self.case else '批量用例执行结果报告'

    def handle(self):
        """ 操作 """
        # 发请求
        res = self.send_msg()
        # 结果校验
        # print(1111111111, self._check_result(res))
        k1, k2 = self._check_result(res)

        # 生成报告
        self._single_html_report(k1, k2)
        # 将报告写入数据库
        self.save_data()
        # # 生成用例集的数据报告
        # result = self.lot_html_report(self.case_list)
        # 删除临时文件
        self.remove_file(self.file_path)
        # return result  # 将用例报告返回给前端展示

    def save_data(self):
        """ 写入数据库 """
        # 将HTML报告写入ITC表
        models.Itc.objects.filter(pk=self.case.pk).update(
            case_html_report=self.read_file(self.file_path)
        )
        # 更新所属的项目
        models.ProjectManage.objects.filter(projectmodel__itc__pk=self.case.pk).update(
            project_status=2
        )

    def _html_runner(self, case):
        """ 生成HTML报告 """

        self.file_path = os.path.join(BASE_DIR, 'static', 'temp.html')
        f = open(self.file_path, 'wb')
        HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=self.case_title,
            description=self.case_desc,
        ).run(case)

    def _single_html_report(self, k1, k2):
        """ 生成单个用例报告 """
        test_case = TesCase()
        test_case.k1, test_case.k2 = k1, k2
        self.case_list.append(test_case)
        self._html_runner(test_case)

    def lot_html_report(self):
        """ 生成所有用例集合 """
        suite = unittest.TestSuite()
        suite.addTests(self.case_list)
        # 生成用例报告
        self._html_runner(suite)
        html_content = self.read_file(self.file_path)

        return html_content


    def send_msg(self):
        """ 发请求 """
        return requests.request(
            url=self.case.case_url,
            method=self.case.case_method,
            params=self._clear_up_params(),
            headers=self._clear_up_headers(),
            cookies=self._clear_up_cookies()
        ).json()

    def _check_result(self, response_data_msg):
        """ 结果校验，校验失败，返回两个被校验参数 """
        case_expect = self.loads(self.case.case_expect)
        # print(11111111111, case_expect)
        for k, v in case_expect.items():
            if k in response_data_msg and v != response_data_msg[k]:
                return response_data_msg[k], case_expect[k]
        else:
            return 1, 1

    def _clear_up_params(self):
        """ 处理 params """

        if self.case.case_parameters:
            params = self.loads(self.case.case_parameters)
            return {k['key']: k['value'] for k in params}
        else:
            return {}

    def _clear_up_headers(self):
        """ 处理 headers """
        if self.case.case_header:
            headers = self.loads(self.case.case_header)
            return {k['key']: k['value'] for k in headers}
        else:
            return {}

    def _clear_up_cookies(self):
        """ 处理 cookies 预留接口"""
        if self.case.case_cookies:
            cookies = self.loads(self.case.case_cookies)
            return {k['key']: k['value'] for k in cookies}
        else:
            return {}



def get_case_result(case_list):
    """ 获取用例执行结果 """
    # 根据用例数量开启线程池的数量
    t = ThreadPoolExecutor(cpu_count() * 5)
    l = []
    count = 0
    for case in case_list:
        # print(11111111, case)
        obj = ExecuteCase(case, l).handle()
        t.submit(obj, case)
        count += 1
        yield {"msg": count}
    t.shutdown()
    res = ExecuteCase(case_list=l).lot_html_report()
    yield {"msg": res}





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



# ------------------------------ 顺序执行用例篇 -----------------------------------









class CaseStatistics(object):
    """ 统计用例信息 """
    case_list = models.Itc.objects.all()
    def manage_info(self):
        """ 统计项目情况
            包括，每个项目分类下面有多少项目，每个项目下有多少用例
            返回一个饼图
        """
        manage = models.ProjectManage.objects.values('project_type__project_type').annotate(c=Count('pk'))
        # print(manage) # <QuerySet [{'project_type__project_type': 'selenium', 'c': 1}, {'project_type__project_type': '接口测试', 'c': 2}]>

        return [{"name": item['project_type__project_type'], "value": item['c']} for item in manage], [
            i['project_type__project_type'] for i in manage]
        # return [
        #     [item['project_type__project_type'] for item in manage],
        #     [i['c'] for i in manage]
        # ]

    def case_execute_status(self):
        """ 用例执行状态 """
        case_status_choices = models.Itc.case_status_choices
        '''
         [
                        {value: 335, name: '直接访问'},
                        {value: 310, name: '邮件营销'},
                        {value: 274, name: '联盟广告'},
                        {value: 235, name: '视频广告'},
                        {value: 400, name: '搜索引擎'}
                    ]
        '''
        l1 = [[i[0], i[1], 0] for i in case_status_choices]
        for item in l1:
            for case in self.case_list:
                if case.case_execute_status == item[0]:
                    item[2] += 1
        return [{"value": item[2], "name": item[1]} for item in l1], [i[1] for i in l1]

    def case_pass_rate_info(self):
        """ 用例通过率统计 """
        case_execute_pass_choices = models.Itc.case_execute_pass_choices
        l1 = [[i[0], i[1], 0] for i in case_execute_pass_choices]

        for item in l1:
            for case in self.case_list:
                # print(case.case_execute_pass)
                if case.case_execute_pass == item[0]:
                    item[2] += 1
        # print(l1)
        # print([{"value": i[2], "name": i[1]} for i in l1], [i[1] for i in l1])
        return [{"value": i[2], "name": i[1]} for i in l1], [i[1] for i in l1]






def getCase(caseList):
    """ 获取到case对象列表 """



    worker = Worker()
    suite = unittest.TestSuite()
    count = 0
    for case in caseList:
        case_obj = worker.test_case(case)
        suite.addTest(case_obj)
        count += 1
        yield count

    # 执行用例
    case_report = CreateReport(case_list=caseList)

    file_path = case_report.create_html_report(suite, case)
    file_content = case_report._read_file(file_path)
    response = {
        "html_report_content": file_content,
        "pdf_report": "pdf_report",
        "img_report": "image_report",
        "html_report": "html_report",
    }

    # # 创建 pdf 用例执行结果
    # case_report._make_report(file_content)
    yield response


class CreateReport(object):
    report_path = os.path.join(BASE_DIR, 'static', 'case_result')

    def __init__(self, case_list):
        self.case_list = case_list
        print(1111111111, self.case_list)



    def check_model(self, case_execute_result):
        """ 判断是否通过，修改用例执行结果和执行状态 """
        res = case_execute_result.__dict__['result']
        '''
        [(1, <util.myCase.TesCase testMethod=runTest>, '', 'Traceback (most recent call last):\n  File "M:\\demo\\AT2\\util\\myCase.py", line 130, in runTest\n    self.assertEqual(self.result, self.expect)\nAssertionError: 302 != \'返回百度2222222222\'\n'), 
        (0, <util.myCase.TesCase testMethod=runTest>, '', '')] Itc object
        '''
        for k, v in zip(res, self.case_list):
            # print(111111, k[0], v.pk, v.case_execute_status, v.case_execute_pass)
            # 根据pk，修改执行结果和执行状态，HTTPrunner 1：未通过  0：通过
            if k[0]:  # 用例执行失败
                models.Itc.objects.filter(pk=v.pk).update(case_execute_pass=3, case_execute_status=2)
            else:  # 用例执行成功
                models.Itc.objects.filter(pk=v.pk).update(case_execute_pass=2, case_execute_status=2)

    def create_html_report(self, suite, case):
        # print(111111111111111111111, suite, case)
        Thread(target=self.run_htmltestrunner, args=suite).start()

        self.run_htmltestrunner(suite)
        file_obj = self._write_file(case)
        case_execute_result = HTMLTestRunner.HTMLTestRunner(
            stream=file_obj[0],
            title=str(case.case_model.project) + ' Case Result',
            description='用例执行情况如下:'
        ).run(suite)
        # self.check_model(case_execute_result)

        return file_obj[1]


    def run_htmltestrunner(self, suites):
        """ 为每个用例生成用例报告 """
        for suite, obj_id in zip(suites, self.case_list):
            f = BytesIO()
            # print(2222222222222222, suite, obj_id.case_url, obj_id.case_title, obj_id.pk)
            res = HTMLTestRunner2.HTMLTestRunner(
                stream=f,
                title=str(obj_id.case_title) + "结果报告",
                description='用例执行情况如下:'
            ).run(suite)
            status = res.__dict__['result'][0]   # 如果执行成功status是0，否则是1
            if status:  # 用例执行失败
                models.Itc.objects.filter(pk=obj_id.pk).update(case_execute_pass=3, case_execute_status=2)
            else:  # 用例执行成功
                models.Itc.objects.filter(pk=obj_id.pk).update(case_execute_pass=2, case_execute_status=2)
            # 将生成的HTML结果报告，更新到数据库

            models.Itc.objects.filter(pk=obj_id.pk).update(case_html_report=f.getvalue())






    def _write_file(self, case):
        file_path = os.path.join(self.report_path, 'result.html')
        return open(file_path, 'wb'), file_path

    def _read_file(self, file_path):
        """ 读文件 """
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()

    def _make_report(self, file_content):
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        config_pdf = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF)
        pdfkit.from_file(input=file_content, output_path=os.path.join(self.report_path, 'result.pdf'),
                         configuration=config_pdf)


class Worker(object):

    def getCaseCol(self, case):
        """ 获取用例对象的url，期望值 """
        return case.case_url, case.case_expect, case.case_method

    def sendRequest(self, case_method, case_url):
        """ 发送请求 """

        res = requests.request(method=case_method, url=case_url)
        return res

    def test_case(self, case):
        """ 添加测试类 """
        # 1. 取用例中所需的字段
        case_url, case_expect, case_method = self.getCaseCol(case)
        # 2.发送请求
        response = self.sendRequest(case_method=case_method, case_url=case_url)
        # 3.创建用例对象并返回
        case_obj = TesCase()
        # 将数据库中的用例记录添加到用例中，用于修改数据库的用例执行状态
        case_obj.case = case
        case_obj.result, case_obj.expect = response.status_code, int(
            case_expect) if case_expect.isdigit() else case_expect
        return case_obj








# if __name__ == '__main__':
#     import os
#     import django
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', "AT2.settings")
#     django.setup()




    # suite = unittest.TestSuite()
    # for i in [(200, 200), (300, 300)]:
    #     obj = TesCase()
    #     obj.result, obj.expect = i[0], i[1]
    #     suite.addTest(obj)
    # unittest.TextTestRunner().run(suite)

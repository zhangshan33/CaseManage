from django.db import models

# Create your models here.


import time
from django.db import models
from web import models as web_models


# Create your models here.


class ApmCase(models.Model):
    """ UI测试用例 """
    case_name = models.CharField(max_length=64, default='UI demo', verbose_name='用例名称')
    case_code = models.TextField(verbose_name='用例代码', default='')
    case_html_report = models.TextField(verbose_name='HTML格式的用例执行结果报告', default='')
    case_vest_project = models.ForeignKey(to=web_models.ProjectManage, verbose_name='归属项目', default=None)
    case_priority = models.IntegerField(default=1, verbose_name='测试用例优先级')
    case_create_username = models.CharField(max_length=64, verbose_name='测试用例创建者', default='好心人')
    case_execute_username = models.CharField(max_length=64, verbose_name='测试用例执行人', default='好心人')
    case_execute_pass_choices = (
        (1, "待定"),
        (2, "已通过"),
        (3, "未通过")
    )
    case_execute_pass = models.IntegerField(choices=case_execute_pass_choices, default=1, verbose_name="测试用例执行是否通过")
    case_status_choices = (
        (1, "未执行"),
        (2, "已执行"),
    )
    case_execute_status = models.IntegerField(choices=case_status_choices, default=1, verbose_name='测试用例状态')
    case_execute_time = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                                             verbose_name='测试用例执行时间')
    case_media_report = models.CharField(max_length=64, default='', verbose_name='MP4版的测试报告')

    def __str__(self):
        return self.case_name

    class Meta:
        ordering = ['-case_execute_time']
import time
import hashlib
from django.db import models
from web import models as web_models


# Create your models here.

def config_media(case_name):
    """ 制作媒体文件路径 """
    return hashlib.md5('{}'.format(time.time()).encode()).digest()

class UiCase(models.Model):
    """ UI测试用例 """
    case_name = models.CharField(max_length=64, default='UI demo', verbose_name='用例名称')
    case_code = models.TextField(verbose_name='用例代码', default='')
    # case_html_report = models.TextField(verbose_name='用例执行结果报告', default='')
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
    case_media_report = models.CharField(verbose_name='视频结果目录', default='', max_length=128)

    def __str__(self):
        return self.case_name

    class Meta:
        ordering = ['-case_execute_time']

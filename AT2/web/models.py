import time
from django.db import models
from django.http import JsonResponse


# Create your models here.

# -------------------------- 项目相关 ---------------------------------

class ProjectManage(models.Model):
    """ 项目管理表 """
    project_name = models.CharField(max_length=255, default='', verbose_name='项目名称')
    project_num = models.CharField(max_length=255, default='', verbose_name='项目代号')
    project_start_time = models.DateField(default='', verbose_name='项目开始时间')
    project_stop_time = models.DateField(default='', verbose_name='项目结束时间')
    project_type = models.ForeignKey("ProjectType", on_delete=models.CASCADE, default='', verbose_name='项目类型')
    project_detail = models.CharField(max_length=2048, default='', verbose_name='项目描述')

    project_status_choices = (
        (1, "未执行"),
        (2, "已执行"),
    )
    project_status = models.IntegerField(choices=project_status_choices, default=1, verbose_name='项目状态', )


    def __str__(self):
        return self.project_name


class ProjectModel(models.Model):
    """ 模块类 """
    model_name = models.CharField(max_length=255, default='', verbose_name='模块名称')
    model_num = models.CharField(max_length=255, default='', verbose_name='模块编号')
    project = models.ForeignKey('ProjectManage', on_delete=models.CASCADE, default='', verbose_name='所属项目')
    def __str__(self):
        return self.model_name

class ProjectType(models.Model):
    """ 项目类型 """
    project_type = models.CharField(max_length=64, verbose_name='项目类型')

    def __str__(self):
        return self.project_type


# -------------------------- 以上，项目相关以上 以下，接口测试相关---------------------------------

class Itc(models.Model):
    """ interface testing case 接口测试 """
    # case_name = models.CharField(max_length=64, verbose_name='接口测试用例名称')
    case_model = models.ForeignKey(to="ProjectModel", on_delete=models.CASCADE, verbose_name='接口测试用例所属模块')
    case_desc = models.CharField(max_length=256, default='', verbose_name='用例描述信息')
    case_cookies = models.CharField(max_length=256, default='', verbose_name='cookies')
    case_priority = models.IntegerField(default=1, verbose_name='测试用例优先级')
    case_title = models.CharField(max_length=128, verbose_name='测试用例标题')
    case_html_report = models.TextField(verbose_name='用例执行结果报告', default='')
    case_url = models.CharField(max_length=255, verbose_name='测试用例地址')
    case_header = models.CharField(max_length=255, verbose_name='测试用例header')
    case_parameters = models.CharField(max_length=255, verbose_name='测试用例参数')
    case_method = models.CharField(max_length=64, verbose_name='测试用例请求方式')
    case_expect = models.CharField(max_length=1024, verbose_name='测试用例期望值')
    case_create_username = models.CharField(max_length=64, verbose_name='测试用例创建者')
    case_execute_username = models.CharField(max_length=64, verbose_name='测试用例执行人')
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
    case_execute_time = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), verbose_name='测试用例执行时间')

    def __str__(self):
        return self.case_title

    class Meta:
        ordering = ['-case_execute_time']

# -------------------------- 以上，接口测试相关---------------------------------





class Testss(models.Model):
    # med = models.FileField(upload_to='ui/', null=True, blank=True)
    name = models.CharField(max_length=64, default='')






# jsonpath_rw

```python
from  jsonpath_rw import parse
```


```
pip install dwebsocket
pip install requests
```

# ui
ui app负责处理ui自动化这一块的app

# apm
amp是移动端针对appium自动化相关的APP


# codemirror
官网: https://codemirror.net/

下载链接: https://codemirror.net/codemirror.zip
# Bootstrap-checkbox
官网：https://vsn4ik.github.io/bootstrap-checkbox/
用法：
需要引入css和js样式
```html
<link rel="stylesheet" href="{% static 'css/checkbox.min.css' %}">
<script src="{% static 'js/bootstrap-checkbox.min.js' %}"></script>
// 示例
<div class="el-checkbox el-checkbox-green">
    <label class="el-checkbox el-checkbox-green">
        <input type="checkbox" title="全选">
        <span class="el-checkbox-style pull-right"></span>
    </label>
</div>
```

# bootstrap样式
1. 输入框组
```html
<div class="input-group">
    <span class="input-group-addon">用例名:</span>
    <input type="text" class="form-control" placeholder="为用例起个名吧">
    <span class="input-group-addon">保存用例</span>
</div>
```
2. 警告，提示
```html
<div class="alert alert-warning alert-dismissible" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
  <strong>Warning!</strong> Better check yourself, you're not looking too good.
</div>
```

# 视频处理
https://juejin.im/post/5d44024be51d4561ab2be985

# pyecharts
echarts官网：https://pyecharts.org/
github： https://github.com/pyecharts/pyecharts
模板：位于 pyecharts.render.templates


# 前端反射的应用

```html
$(".operationType").on('click', 'li a', function () {
            if (typeof(window[$(this).attr('operation')]) == 'function') {
               window[$(this).attr('operation')]()
            }
        });
```

# sweetalert
官网：https://sweetalert.bootcss.com/
github:https://github.com/t4t5/sweetalert

用前引入
```html

<link rel="stylesheet" href="{% static 'sweetalert/sweetalert.min.css' %}">
<script src="{% static 'sweetalert/sweetalert.min.js' %}"></script>
<!-- bootcnd -->
<link href="https://cdn.bootcss.com/sweetalert/1.1.3/sweetalert.min.css" rel="stylesheet">
<script src="https://cdn.bootcss.com/sweetalert/1.1.3/sweetalert.min.js"></script>
```
- 自动消失的弹出框
```html
swal({
    title: "Successful",
    text: "用例保存成功",
    timer: 2000,
    showConfirmButton: false
});
```


# orm以时间排序
```python
import time
from django.db import models
from web import models as web_models
class UiCase(models.Model):
    """ UI测试用例 """
    case_name = models.CharField(max_length=64, default='UI demo', verbose_name='用例名称')
    case_code = models.TextField(verbose_name='用例代码', default='')
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

    def __str__(self):
        return self.case_name

    class Meta: 
        # 以时间排序，时间由近到远排序，别忘了字段中的中横
        ordering = ['-case_execute_time']
```


# requirements

- 生成requirements.txt文件
```
pip freeze > requirements.txt
```
- 从requirements.txt文件安装依赖
```
pip install -r requirements.txt
```

# 常见报错
- selenium.common.exceptions.WebDriverException: Message: An unknown server-side error occurred while processing the command. Original error: EPIPE: broken pipe, write


import time
import os
import json
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from util import myForms
from web import models
from dwebsocket.decorators import accept_websocket
# from pyecharts.charts import Pie
# from pyecharts import options as opt
from util import myCase
from util import tools as public_tools
from django.db.models import Sum, Avg, Count


# Create your views here.


def index(request):
    """ 项目首页index """
    case_statistics = myCase.CaseStatistics()
    # 用例通过率

    # 项目情况

    manage = case_statistics.manage_info()
    # print(manage)  # ([{'name': 'selenium', 'value': 1}, {'name': '接口测试', 'value': 2}], ['selenium', '接口测试'])
    case_execute_status = case_statistics.case_execute_status()
    # print(case_execute_status)  # ([{'value': 0, 'name': '未执行'}, {'value': 8, 'name': '已执行'}], ['未执行', '已执行'])
    case_pass_rate_info = case_statistics.case_pass_rate_info()
    # print(case_pass_rate_info)  # ([{'value': 0, 'name': '待定'}, {'value': 8, 'name': '已通过'}, {'value': 0, 'name': '未通过'}], ['待定', '已通过', '未通过'])
    return render(request, 'index.html', {
        "manage": manage,
        "case_execute_status": case_execute_status,
        "case_pass_rate_info": case_pass_rate_info

    })
    # return render(request, 'index.html')


# --------------- 项目管理相关 ------------------


def manage(request):
    """ 项目管理主页 """
    project_obj = models.ProjectManage.objects.all()
    # print(111111111, project_obj)
    if project_obj:
        for i in project_obj:
            for k in i.project_status_choices:
                if k[0] == i.project_status:
                    i.project_status = k[1]
                    break
        return render(request, 'manage.html', {'project_obj': project_obj})
    else:
        return render(request, 'manage.html', {'project_obj': ''})


def manage_add(request):
    """ 添加项目 """
    if request.method == "POST":
        form = myForms.ManageModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')
        else:
            return render(request, 'manage_add.html', {"form": form})
    else:
        model_form = myForms.ManageModelForm()
        return render(request, 'manage_add.html', {"form": model_form})


def manage_delete(request, del_id):
    """ 删除项目 """
    models.ProjectManage.objects.filter(id=del_id).delete()
    return redirect('/index/')


def manage_edit(request, edit_id):
    """ 编辑项目 """
    edit_obj = models.ProjectManage.objects.filter(id=edit_id).first()
    if request.method == 'POST':
        form = myForms.ManageModelForm(request.POST, instance=edit_obj)
        if form.is_valid():
            form.save()
            return redirect('/index/')
        else:
            return render(request, 'manage_edit.html', {"form": form})
    else:
        form = myForms.ManageModelForm(instance=edit_obj)
        return render(request, 'manage_edit.html', {"form": form})


# --------------- 模块相关 ------------------


def md_list(request, id):
    """ 模块列表 """
    obj = models.ProjectManage.objects.filter(pk=id).first()
    md_obj = obj.projectmodel_set.all()

    if md_obj:
        return render(request, 'md_list.html', {"obj": md_obj, "project": obj})
    else:
        return render(request, 'md_list.html', {"project": obj})


def md_add(request, id):
    """ 新增模块，只有接口测试的项目有下属模块 """
    if request.method == "POST":
        form = myForms.MdModelForm(request.POST)
        if form.is_valid():
            obj = models.ProjectModel.objects.create(**form.cleaned_data, project_id=id)
            obj.save()
            # form.save()
            return render(request, 'md_list.html', {"form": form, "id": id})
        else:
            return render(request, 'md_add.html', {"form": form})

    else:
        # print(222222, id)
        form = myForms.MdModelForm()
        return render(request, 'md_add.html', {"form": form, "id": id})


def md_edit(request, id):
    """ 编辑模块 """

    md_obj = models.ProjectModel.objects.filter(id=id).first()
    if request.method == "POST":
        form = myForms.MdModelForm(request.POST, instance=md_obj)
        if form.is_valid():
            form.save()
        return redirect('/md_list/{}'.format(md_obj.project_id))
    else:
        form = myForms.MdModelForm(instance=md_obj)
        print(1111111111, md_obj, id)
        return render(request, 'md_edit.html', {"form": form, 'pk': id})


def md_delete(request, id):
    """ 删除模块 """

    obj = models.ProjectModel.objects.filter(id=id).first()
    md_id = obj.project_id
    obj.delete()
    return redirect('/md_list/{}'.format(md_id))


# --------------- 接口测试用例 ------------------

def case_list(request, id):
    pass


def case_add(request):
    if request.method == "POST":
        models.Itc.objects.create(
            case_model_id=request.POST.get('case_model'),
            case_priority=request.POST.get('case_priority'),
            case_title=request.POST.get('case_title'),
            case_url=request.POST.get('case_url'),
            case_header=request.POST.get('case_header'),
            case_parameters=request.POST.get('case_parameters'),
            case_method=request.POST.get('case_method'),
            case_expect=request.POST.get('case_expect'),
            case_create_username=request.POST.get('case_create_username'),
            case_execute_username=request.POST.get('case_execute_username'),
        )
        return HttpResponse('OK')
    else:
        project_obj = models.ProjectManage.objects.all()
        return render(request, 'case/case_add.html', {"project_obj": project_obj})


def choices_model(request):
    """ 项目与模块2级联动 """
    if request.method == "POST":
        id = request.POST.get('id')
        obj = models.ProjectManage.objects.filter(pk=id).first()
        data_list = [{"model_name": i.model_name, "id": i.id} for i in obj.projectmodel_set.all()]
        return JsonResponse({"obj": data_list})
    else:
        pass


def case_edit(request, id):
    if request.method == 'POST':
        models.Itc.objects.filter(pk=id).update(
            case_model_id=request.POST.get('case_model'),
            case_priority=request.POST.get('case_priority'),
            case_title=request.POST.get('case_title'),
            case_url=request.POST.get('case_url'),
            case_header=request.POST.get('case_header'),
            case_parameters=request.POST.get('case_parameters'),
            case_method=request.POST.get('case_method'),
            case_expect=request.POST.get('case_expect'),
            case_create_username=request.POST.get('case_create_username'),
            case_execute_username=request.POST.get('case_execute_username'),
            case_execute_pass=1
        )
        return HttpResponse('interface')
    else:
        obj = models.Itc.objects.filter(pk=id).first()
        project_obj = models.ProjectManage.objects.all()
        obj.case_header = json.loads(obj.case_header)
        obj.case_parameters = json.loads(obj.case_parameters)
        return render(request, 'case/case_edit.html', {'obj': obj, "project_obj": project_obj})


def case_delete(request, id):
    print(request, id)
    models.Itc.objects.filter(pk=id).delete()
    return redirect('/interface/')


def interface(request):
    """ 接口测试主页 """
    if request.method == 'POST':
        pass
    else:
        project_obj = models.ProjectManage.objects.filter(project_type__project_type='接口测试')
        fields = models.Itc._meta.fields
        interface_obj = models.Itc.objects.all()[:10]
        public_tools.check_choices(models.Itc.case_execute_pass_choices, interface_obj, models.Itc.case_execute_pass)
        public_tools.check_choices(models.Itc.case_status_choices, interface_obj, models.Itc.case_execute_status)
        return render(request, 'interface/interface_index.html', {
            "project_obj": project_obj,
            "fields": fields,
            "interface_obj": interface_obj,
        })


def interface_choices(request):
    """ 接口的2级联动 """
    if request.method == "POST":
        # print(1111111111, request.POST)
        id = request.POST.get('project_pk')
        model_msg = request.POST.get('model_pk')
        if model_msg:  # 如果有选择模块，过滤某个项目下的某个模块下的用例
            obj = models.Itc.objects.filter(case_model__project_id=id, case_model_id=model_msg)
        else:  # 如果模块的值为空，则是获取某个项目下的所有用例
            obj = models.Itc.objects.filter(case_model__project_id=id)

        for i in obj:
            # print(i, i.case_execute_status, i.get_case_execute_status_display())
            for item in models.Itc.case_status_choices:
                if i.case_execute_status == item[0]:
                    i.case_execute_status = item[1]
                    break
            for item2 in models.Itc.case_execute_pass_choices:
                if i.case_execute_pass == item2[0]:
                    i.case_execute_pass = item2[1]
                    break
        project_list = models.ProjectManage.objects.filter(pk=id).first().projectmodel_set.all()
        # print(111111, project_list, obj)  # 111111 <QuerySet [<ProjectModel: 模块1>, <ProjectModel: 模块2>]> <QuerySet [<Itc: Itc object>, <Itc: Itc object>]>

        return JsonResponse({"modelList": serialize('json', project_list), "caseList": serialize('json', obj)})

    else:
        pass


@accept_websocket
def TestCase(request):
    """ 接口测试入口，接收前端传来的单个或者批量的用例id，然后测试用例并生成测试报告 """
    if request.is_websocket():
        message = request.websocket.wait()
        result = json.loads(message)
        print(result)
        res = models.Itc.objects.filter(pk__in=result['case_list'])
        genCaseResult = myCase.getCase(res)
        while 1:
            if message:
                for g in genCaseResult:
                    request.websocket.send(json.dumps({"msg": g}))
                    time.sleep(3)
            else:
                request.websocket.close()
    else:
        return JsonResponse({"OK": "666"})


@accept_websocket
def TestCase1(request):
    """ 接口测试入口，接收前端传来的单个或者批量的用例id，然后测试用例并生成测试报告 """
    if request.is_websocket():
        message = request.websocket.wait()
        result = json.loads(message)
        # print(result)
        res = models.Itc.objects.filter(pk__in=result['case_list'])
        genCaseResult = myCase.getCase(res)
        while 1:
            if message:
                for g in genCaseResult:
                    request.websocket.send(json.dumps({"msg": g}))
                    time.sleep(3)
            else:
                request.websocket.close()
    else:
        return JsonResponse({"OK": "666"})



def get_interface_case_report(request):
    """ 处理接口测试报告 """
    if request.method == "POST":
        pk = request.POST.get('pk')
        obj = models.Itc.objects.filter(pk=pk).first()
        print(type(obj.case_html_report), obj.case_html_report)
        return JsonResponse({'obj': obj.case_html_report})


# from signal import pizza_done
def test(request):
    """ 测试使用，与本项目无关 """
    if request.method == 'POST':
        result = request.POST.get('a')
        print(result)
        # f = open(r'C:\Users\Anthony\Desktop\selenium_result.mp4', 'rb')
        # models.Testss.objects.filter(pk=20).update(
        #     med=f.read()
        # )
        return HttpResponse('OK')
    else:
        # res = models.Itc.objects.filter(pk__in=['13', '11'])
        # myCase.get_case_result(res)
        # obj = models.ProjectManage.objects.filter(projectmodel__itc__pk=13).first()
        # print(obj)
        '''
        11111111111 <class 'web.models.Testss'> {'signal': <django.db.models.signals.ModelSignal object at 0x03263410>, 'instance': <Testss: Testss object>, 'created': True, 'update_fields': None, 'raw': False, 'using': 'default'}
        '''
        models.Testss.objects.create(name='张开')
        # print(11111111111111111111111111111111111111111111111111111111111)
        obj = models.Testss.objects.filter(pk=22).first()
        obj.name = '3333'
        obj.save()




        return HttpResponse("OK")

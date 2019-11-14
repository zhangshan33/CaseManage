import os
import json
import time
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, FileResponse
from ui.util import tools as ui_tools
from web import models as web_models
from ui import models as ui_models
from django.core import serializers
from util import myCase
from dwebsocket.decorators import accept_websocket

def ui_index(request, pk=0):
    """ UI测试主页 """
    if request.method == 'POST':
        pass
        # pk = request.POST.get('pk')
        #
        # result = ui_models.UiCase.objects.filter(case_vest_project=pk)
        # for item in ui_models.UiCase.case_execute_pass_choices:
        #     for case in result:
        #         if case.case_execute_pass == item[0]:
        #             case.case_execute_pass = item[1]
        #
        # return JsonResponse({"case": serializers.serialize('json', result)})
    else:
        result = web_models.ProjectManage.objects.filter(project_type__project_type="selenium")
        if int(pk):  # 项目结果过滤
            ui_case = ui_models.UiCase.objects.filter(case_vest_project_id=pk)
        else:
            ui_case = ui_models.UiCase.objects.all()[:10]
        myCase.check_choices(ui_models.UiCase.case_execute_pass_choices, ui_case, ui_models.UiCase.case_execute_pass)
        myCase.check_choices(ui_models.UiCase.case_status_choices, ui_case, ui_models.UiCase.case_execute_status)
        return render(request, 'ui/ui_index.html', {"case_vest_project_name": result, 'ui_case': ui_case})


def ui_update_case(request, pk=0):
    """ 新增，修改， 执行于一身的函数 """

    if request.method == "POST":
        data = dict(case_code=request.POST.get('case_code'),
                    case_name=request.POST.get('case_name'),
                    case_vest_project_id=request.POST.get('case_vest_project'),
                    case_execute_pass=request.POST.get('case_execute_pass'),
                    case_execute_status=2,
                    case_execute_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        if int(pk):  # 更新
            # print(2222, data)
            ui_models.UiCase.objects.filter(pk=pk).update(**data)
        else:
            ui_models.UiCase.objects.create(**data)
        return HttpResponse('OK')
    else:
        project_obj = web_models.ProjectManage.objects.filter(project_type__project_type='selenium')
        ui_case_obj = ui_models.UiCase.objects.filter(pk=pk).first()
        ui_case_obj_case_code = [i for i in ui_case_obj.case_code] if ui_case_obj else []
        return render(request, 'ui/ui_update.html', {
            "project_obj": project_obj,
            "ui_case_obj": ui_case_obj,
            "ui_case_obj_case_code": ui_case_obj_case_code
        })


def ui_delete_case(request, pk):
    # print(request, pk)
    ui_models.UiCase.objects.filter(pk=pk).delete()
    return redirect('/ui/ui_index/0')


# def ui_add_case(request):
#     """ 测试用例修改 """
#     if request.method == "POST":
#         case_code = request.POST.get('case_code')
#         case_name = request.POST.get('case_name')
#         case_vest_project = request.POST.get('case_vest_project')
#         ui_models.UiCase.objects.create(
#             case_name=case_name,
#             case_code=case_code,
#             case_vest_project_id=case_vest_project
#         )
#         # print(case_name, case_code, case_vest_project)
#         return HttpResponse('ok')
#     else:
#         project_result = web_models.ProjectManage.objects.filter(project_type__project_type='selenium')
#         return render(request, 'ui/ui_add.html', {"res": project_result})
#
#
# def ui_edit_case(request, pk):
#     """ 修改ui测试用例 """
#     if request.method == "POST":
#         case_code = request.POST.get('case_code')
#         case_name = request.POST.get('case_name')
#         case_vest_project = request.POST.get('case_vest_project')
#         print(11111, case_name, case_code, case_vest_project)
#         ui_models.UiCase.objects.filter(pk=pk).update(
#             case_name=case_name,
#             case_code=case_code,
#             case_vest_project=case_vest_project,
#         )
#         return HttpResponse('ok')
#     else:
#         project_result = web_models.ProjectManage.objects.filter(project_type__project_type='selenium')
#         res = ui_models.UiCase.objects.get(pk=pk)
#         return render(request, 'ui/ui_edit.html', {"res": [i for i in res.case_code], "case": res, 'project': project_result})

@accept_websocket
def ui_execute(request):
    """ 执行Python代码并返回执行结果 """
    if request.is_websocket():
        execute_obj = ui_tools.Execute()
        msg = request.websocket.wait()
        # print(1111111, type(msg), json.loads(msg))
        execute_obj._write_file(json.loads(msg)['case_code'])
        # execute_obj._start_avi()
        # try:
        while 1:
            if msg:
                result = execute_obj.execute_file(json.loads(msg)['screen_status'], json.loads(msg)['case_id'])
                for g in result:
                    # print(11111111111, type(g), g)
                    request.websocket.send(g)
                else:
                    request.websocket.close()
                    # execute_obj._stop_avi()
                    break
        # except Exception as e:
        #     request.websocket.close()
        #     print(3333333333333333333333333, e)
    # if request.method == "POST":
    #     value = request.POST.get('value')  # <type: str>
    #     exe_obj = tools.Execute()
    #     exe_obj._write_file(value)
    #     result = exe_obj.execute_file()
    #     return HttpResponse(result)
    else:
        return HttpResponse('非法请求')


def ui_execute_websocket(request):
    """ 执行Python代码并返回执行结果， websocket版 """
    pass


def ui_download_file(request):
    """ 下载逻辑 """
    if request.method == "POST":
        case_pk_json = request.POST.get('case_pk')
        case_pk = json.loads(case_pk_json)
        # print(case_pk)
        case_obj = ui_models.UiCase.objects.filter(pk__in=case_pk)
        # print(case_obj)
        ui_tools.MakePackage(case_obj).get_zip_file()

        return HttpResponse('OK')
    else:
        return HttpResponse('非法请求')



def ui_get_case_report(request):
    """ 展示用例结果报告 """
    if request.method == 'POST':
        pk = request.POST.get('pk')
        obj = ui_models.UiCase.objects.filter(pk=pk).first()
        print(obj.case_media_report)
        return JsonResponse({'case_path': obj.case_media_report, 'case_name': obj.case_name})



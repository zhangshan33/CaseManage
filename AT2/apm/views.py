import json
import time
from django.shortcuts import render, redirect, HttpResponse, Http404
from apm import models as apm_models
from web import models as web_models
from dwebsocket.decorators import accept_websocket
from util import tools as pubic_tools
from apm.util import tools as apm_tools
from collections import Generator

def apm_index(request, pk=0):
    """ appium 主页 """
    if request.method == 'POST':
        return HttpResponse('OK')
    else:
        result = web_models.ProjectManage.objects.filter(project_type__project_type='移动端测试')
        print(1111, result)
        if int(pk):
            case_obj = apm_models.ApmCase.objects.filter(case_vest_project_id=pk)
        else:
            case_obj = apm_models.ApmCase.objects.all()[:10]
        # print(2222222222, apm_case)
        pubic_tools.check_choices(apm_models.ApmCase.case_execute_pass_choices, case_obj, apm_models.ApmCase.case_execute_pass)
        pubic_tools.check_choices(apm_models.ApmCase.case_status_choices, case_obj, apm_models.ApmCase.case_execute_status)
        return render(request, 'apm/apm_index.html', {"case_vest_project_name": result, "case_obj": case_obj})



def apm_update(request, pk=0):
    """ 新增、修改 appium 用例 """
    # print(1111111111, request, pk)
    if request.method == 'POST':
        data = dict(case_code=request.POST.get('case_code'),
                    case_name=request.POST.get('case_name'),
                    case_vest_project_id=request.POST.get('case_vest_project'),
                    case_execute_pass=request.POST.get('case_execute_pass'),
                    case_execute_status=2,
                    case_execute_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        # print(1111111111111, data)
        if int(pk):  # 更新
            # print(2222, data)
            apm_models.ApmCase.objects.filter(pk=pk).update(**data)
        else:
            apm_models.ApmCase.objects.create(**data)
        return HttpResponse('OK')
    else:

        project_obj = web_models.ProjectManage.objects.filter(project_type__project_type='移动端测试')
        apm_case_obj = apm_models.ApmCase.objects.filter(pk=pk).first()
        apm_case_obj_case_code = [i for i in apm_case_obj.case_code] if apm_case_obj else []
        # 获取可用的devices 列表
        devices_list = apm_tools.ExecuteDevices().get_devices()
        # print(11111111111111111111111, devices_list)
        return render(request, 'apm/apm_update.html', {
            "project_obj": project_obj,
            "apm_case_obj": apm_case_obj,
            "apm_case_obj_case_code": apm_case_obj_case_code,
            'devices_list': devices_list,
        })

@accept_websocket
def apm_execute_cmd_command(request):
    if request.is_websocket():
        print('websocket connection....')
        msg = request.websocket.wait()  # 接收前端发来的消息
        # print(11111111111, type(msg), json.loads(msg))  # b'["1","2","3"]' <class 'bytes'> ['1', '2', '3']
        while 1:
            if msg:
                result = apm_tools.ExecuteDevices().get_execute_handle(json.loads(msg))
                print(222222222222, result)
                for g in result:
                    # print(111111111111111, g)
                    # request.websocket.send(json.dumps({"msg": g.strip().decode('gbk')}))  # 向客户端发送数据
                    request.websocket.send(g)  # 向客户端发送数据
                    # time.sleep(0.2)  # 每0.2秒发一次
                else:
                    # request.websocket.send(result)
                    request.websocket.close()
                    break
    else:  # 如果是普通的请求
        return Http404('错误的页面')



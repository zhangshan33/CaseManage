from django.shortcuts import render

# Create your views here.

def bm_index(reqeust):
    """ 后台管理主页 """
    return render(reqeust, 'bm/bm_index.html')


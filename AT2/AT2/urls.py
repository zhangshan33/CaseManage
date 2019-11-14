"""AT2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from web import views
from django.views.static import serve
from django.conf.urls.static import static
from AT2 import settings



from django_pdfkit import PDFView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.test, name='test'),
    url(r'^index/', views.index, name='index'),
    # 项目管理相关
    url(r'^manage/', views.manage, name='manage'),
    url(r'^manage_add/', views.manage_add, name='manage_add'),
    url(r'^manage_delete/(?P<del_id>\d+)$', views.manage_delete, name='manage_delete'),
    url(r'^manage_edit/(?P<edit_id>\d+)?', views.manage_edit, name='manage_edit'),

    # 模块相关，只有接口测试有模块
    url(r'^md_list/(?P<id>\d+)$', views.md_list, name='md_list'),
    url(r'^md_add/(?P<id>\d+)$', views.md_add, name='md_add'),
    url(r'^md_edit/(?P<id>\d+)$', views.md_edit, name='md_edit'),
    url(r'^md_delete/(?P<id>\d+)$', views.md_delete, name='md_delete'),

    # 接口测试相关
    url(r'^interface/', views.interface, name='interface'),
    url(r'^interface_choices/', views.interface_choices, name='interface_choices'),
    url(r'^case_list/(?P<id>\d+)$', views.case_list, name='case_list'),
    url(r'^case_add', views.case_add, name='case_add'),
    url(r'^case_edit/(?P<id>\d+)$', views.case_edit, name='case_edit'),
    url(r'^case_delete/(?P<id>\d+)$', views.case_delete, name='case_delete'),
    url(r'^case/choices_model', views.choices_model, name='choices_model'),
    url(r'^case/testcase', views.TestCase, name='TestCase'),
    url(r'^case/testcase1', views.TestCase1, name='TestCase1'),
    url(r'^case/get_interface_case_report', views.get_interface_case_report, name='get_interface_case_report'),
    url(r'ui/', include('ui.urls')),

    # 移动端相关接口
    url(r'apm/', include('apm.urls')),

    # 后台管理相关接口
    url(r'bm/', include('bm.urls')),

    # 媒体文件
    # url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

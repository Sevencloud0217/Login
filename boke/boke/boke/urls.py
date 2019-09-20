"""boke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('index/',views.index,name='index'),
    path('listpic/',views.listpic),
    path('newslistpic/',views.newslistpic),
    re_path('newslistpic/(?P<type>\w+)/(?P<page>\d+)',views.newslistpic),
    path('base/',views.base),
    path('addariticle/',views.addariticle),
    path('fytest/',views.fytest),
    re_path('xiangxi/(?P<id>\d+)',views.xiangxi),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('reqtest/',views.reqtest),
    path("fromtest/",views.fromtest),
    path("register/",views.register),
    path('ajax_get/',views.ajax_get),
    path('ajax_get_data/',views.ajax_get_data),
    path('ajax_post/',views.ajax_post),
    path('ajax_post_data/',views.ajax_post_data),
    path('checkusername/',views.checkusername),
    path('login/',views.login),
    path('logout/',views.logout),
]



from django.urls import path,re_path,include
from .views import *
# from app01 import views as app01views

urlpatterns = [
    path('index/',index),
    path('addperson/',addperson),
    path('queryset/',queryset),
    path('updata/',updata),
    path('drop/',drop),
    path('addonemore/',addonemore),
    path('getonemore/',getonemore),
    path('updataonemore/',updataonemore),
    path('deleteonemore/',deleteonemore),
    path('manytomanyadd/',manytomanyadd),
    path('manytomanyget/',manytomanyget),
    path('manytomanyupdate/',manytomanyupdate),
    path('manytomanydelete/',manytomanydelete),
    path('jhtest/',jhtest),
    path('Ftest/',Ftest),
    path('Qtest/',Qtest),
]

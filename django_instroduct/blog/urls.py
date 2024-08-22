# 配置路由

from django.urls import path, include

from . import views

#

urlpatterns = [
    path('hello_world', views.hello_world),
    path('hello_world1', views.hello_world1)
]
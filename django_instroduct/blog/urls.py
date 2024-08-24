# 配置路由

from django.urls import path, include

# from blog.views import views
from . import views

#

urlpatterns = [
    path('hello_world', views.hello_world),
    path('content', views.article_content),
    path('index', views.get_index_page),
    # path('detail', views.get_detail_page)
    # 获取单独页面URL路径
    path('detail/<int:article_id>', views.get_detail_page)
]
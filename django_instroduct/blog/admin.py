from django.contrib import admin

# Register your models here.

# 是后台管理工具, 读取定义的模型元数据,提供页面管理能力
# python .\manage.py createsuperuser 创建超级管理员账号和密码


# 将models注册到admin里面
from .models import Article

# 模型注册
admin.site.register(Article)

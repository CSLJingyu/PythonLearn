from django.db import models


# Create your models here.
# 模型定义

class Article(models.Model):
    # 文章ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章内容
    content = models.TextField()
    # 文章日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # 返回文章的title
        return self.title

    # 1.写完上面后,要进行文件的迁移, 输入python .\manage.py makemigrations,得到migrations下面的0001_initial.py
    # 2.运行上述文件 python .\manage.py migrate, 这个操作是运行迁移文件,将迁移文件的内容同步到数据库里面去
    # 3.通过python manage.py shell使用来创建一个Article模型对象, 实现一些测试和开发

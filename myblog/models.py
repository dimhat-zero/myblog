# -*- coding: UTF-8 -*-
from django.db import models


# id 是自动的
# null 是否可为空，默认为False
# blank 是否允许空白，默认为False
# default 默认值
# 'self' 加自己为外键
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, default="新用户")
    email = models.EmailField()
    register_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # 是否激活
    is_staff = models.BooleanField(default=False)  # 是否管理员

    def __str__(self):
        return self.nickname


class Article(models.Model):
    author = models.ForeignKey(User)  # 外键
    publication_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now_add=True)  # 修改时间
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.CharField(max_length=100, blank=True)  # 标签
    types = models.CharField(max_length=20)  # 文章类型
    status = models.CharField(max_length=20)  # 文章状态
    read_count = models.IntegerField(default=0)  # 阅读总数
    comment_count = models.IntegerField(default=0)  # 评论总数

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article)  # 外键
    comment_parent = models.ForeignKey('self', null=True)  # 外键
    user = models.ForeignKey(User, null=True)  # 发布人，没登录为空
    author = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.CharField(max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
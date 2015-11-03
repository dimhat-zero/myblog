from django.http import HttpResponse
from django.shortcuts import render_to_response
from myblog.models import User, Article, Comment


# 首页，显示所有文章
def index(request):
    return render_to_response('index.html', {'articles': Article.objects.all()})


# 注册用户
def register(request):
    return HttpResponse("chinese is error")


# 登录
def login(request):
    return HttpResponse("chinese is error")


def hello(request):
    return HttpResponse("Hello world")

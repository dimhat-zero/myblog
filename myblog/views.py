# -*- coding: UTF-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from myblog.models import User, Article, Comment
from django.template import RequestContext

# 首页，显示所有文章
def index(request):
    return render_to_response('index.html', {'articles': Article.objects.all()})


def hello(request):
    return HttpResponse("Hello world")


# 后台管理页面
def manage(request):
    if "user_id" not in request.session:
        return HttpResponseRedirect("login")

    return render_to_response('manage.html',context_instance=RequestContext(request))

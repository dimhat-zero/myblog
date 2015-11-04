from django.http import HttpResponse
from django.shortcuts import render_to_response
from myblog.models import User, Article, Comment


# 首页，显示所有文章
def index(request):
	return render_to_response('index.html', {'articles': Article.objects.all()})


# 管理页面
def manage(request):
	username = request.session["username"]
	nickname = request.session["nickname"]
	print("%s %s" %(username,nickname))
	return render_to_response('manage.html',{'username':username,'nickname':nickname})



def hello(request):
	return HttpResponse("Hello world")

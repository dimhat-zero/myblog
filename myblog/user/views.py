# -*- coding: UTF-8 -*-
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from myblog.models import User
from myblog.user.forms import RegisterForm, LoginForm,ModifyForm,UserForm
from django.template import RequestContext
from django.shortcuts import get_object_or_404

# register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            u = User(
                username=cd['username'],
                password=cd['password'],
                email=cd['email']
            )
            u.save()
            return HttpResponseRedirect('/register_success')
    else:
        form = RegisterForm(
            initial={'my_code': 'guess'}
        )
    return render_to_response('user/register.html', {'form': form},
                              context_instance=RequestContext(request))


def register_success(request):
    assert request.method == 'GET'
    return render_to_response('user/register_success.html')


# login
def login(request):
    message = ""
    if "user_id" in request.session:
        message = u"已经登陆"
        return HttpResponseRedirect("/manage")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                u = User.objects.get(username=cd['username'])
            except User.DoesNotExist:
                message = u"用户名不存在"
            else:
                if u.password != cd['password']:
                    message = u"密码不正确"
                elif u.is_active==False:
                    message = u"账号被冻结"
                else:
                    request.session["user_id"] = u.id
                    request.session["username"] = u.username
                    request.session["nickname"] = u.nickname
                    request.session["is_staff"] = u.is_staff
                    return HttpResponseRedirect('/manage')
    else:
        form = LoginForm()

    return render_to_response("user/login.html", {'form': form, 'message': message},
                                  context_instance=RequestContext(request))


# 退出登录
def logout(request):
    try:
        del request.session["user_id"]
        del request.session["username"]
        del request.session["nickname"]
        del request.session["is_staff"]
    except:
        pass
    return HttpResponseRedirect("login")


def user_detail(request,id):
    u = get_object_or_404(User,pk=id)
    if request.method == 'POST':
        form = ModifyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            u.nickname = cd["nickname"]
            u.email = cd["email"]
            u.is_active = cd["is_active"]
            u.is_staff = cd["is_staff"]
            u.save()
            return HttpResponseRedirect("/users/%s" %id)
    else:
        form = ModifyForm(instance=u)
    return render_to_response("user/user_detail.html",{'form':form,'user':u},
                                  context_instance=RequestContext(request))

def user_list(request):
    pass
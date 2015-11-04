from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from myblog.models import User
from myblog.user.forms import RegisterForm,LoginForm
from django.template import RequestContext


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

def test_json(request):
    u = User(username="json",password="json2")
    str = json.dumps(u)
    return HttpResponse(str)

# login
def login(request):
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                u = User.objects.get(username=cd['username'])
            except User.DoesNotExist:
                message = "账号不存在"
            else:
                if u.password != cd['password']:
                    message = "密码错误"
                else:
                    request.session["user_id"] = u.id
                    request.session["username"] = u.username
                    request.session["nickname"] = u.nickname
                    return HttpResponseRedirect('/manage')
    else:
        form = LoginForm()
    return render_to_response("user/login.html", {'form': form,'message':message},
                              context_instance=RequestContext(request))

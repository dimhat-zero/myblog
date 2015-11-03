from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from myblog.models import User
from myblog.user.forms import RegisterForm
from django.template import RequestContext


# ×¢²áÓÃ»§
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
            return HttpResponseRedirect('/register_success/')
    else:
        form = RegisterForm(
            initial={'my_code': 'guess'}
        )
    return render_to_response('user/register.html', {'form': form},
                              context_instance=RequestContext(request))

def register_success(request):
    assert request.method == 'GET'
    return render_to_response('user/register_success.html')

# µÇÂ¼
def login(request):
    return HttpResponse("no ok")

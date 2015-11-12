# -*- coding: UTF-8 -*-
from django.http import HttpResponseRedirect


def comment_add(request,id):
    #go to comment location
    if request.method=='GET':
        return HttpResponseRedirect("/article"+id+"#comment")
    #add comment
    else:
        pass

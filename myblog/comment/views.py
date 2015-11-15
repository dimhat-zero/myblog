# -*- coding: UTF-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from myblog.comment.forms import CommentForm
from myblog.models import Comment,Article,User

def comment_add(request,id):
    #add comment
    if request.method=='POST':
        form = CommentForm(request.POST)
        print("is be")
        if form.is_valid():
            print("is ok")
            cd = form.cleaned_data
            #comment_parent=Comment(id=cd["comment_parent_id"]),
            post = Comment(
                article=Article(id=id),
                user = User(id=cd["user_id"]),
                email = cd["email"],
                author = cd["author"],
                content = cd["content"]
            )
            if cd["comment_parent_id"] != None:
                post.comment_parent = Comment(id=cd["comment_parent_id"])

            post.save()

        print("%r" % form.errors)

    return HttpResponseRedirect("/articles/%d#comment" % int(id))


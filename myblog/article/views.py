# -*- coding: UTF-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from myblog.models import Article, User
from myblog.article.forms import ArticleForm
from django.template import RequestContext


def article_detail(request, id):
    if request.method == 'POST':
        # update form
        pass
    elif request.method == 'GET':
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            raise Http404
        else:
            article.read_count+=1
            article.save()
        return render_to_response('article/article_detail.html', {'article': article})
    else:
        raise Http404


def article_list(request):
    page = request.GET.get('page', '1')
    per_page = request.GET.get('per_page', '10')
    # trans to int
    page = int(page)
    per_page = int(per_page)

    start = (page-1)*per_page
    end = start + per_page
    articles = Article.objects.all()[start:end]
    return render_to_response('article/article_list.html',{'articles':articles})


def post_article(request):
    user_id = request.session["user_id"]
    print("haha %s" % user_id)
    if(user_id==None):
        return HttpResponseRedirect("/login")
    if (request.method == 'POST'):
        form = ArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            article = Article(
                title=cd["title"],
                content=cd["content"],
                tags=cd["tags"],
                types=cd["types"],
                author=User(id=user_id)
            )
            article.save()
            return HttpResponseRedirect("/articles/%d" % article.id)
    else:
        form = ArticleForm()
    return render_to_response("article/post_article.html", {'form': form},
                              context_instance=RequestContext(request))

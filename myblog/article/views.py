# -*- coding: UTF-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from myblog.models import Article, User
from myblog.article.forms import ArticleForm
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


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
            article.read_count += 1
            article.save()
        return render_to_response('article/article_detail.html', {'article': article})
    else:
        raise Http404


def post_list(request):
    page_no = request.GET.get('page', '1')
    per_page = request.GET.get('per_page', '10')

    # 获取分页器
    posts = Article.objects.all()
    paginator = Paginator(posts, per_page)
    # 获取page_no页
    page = paginator.page(page_no)
    page_tot = paginator.num_pages  # 总页数
    # 前一页和后一页
    has_previous = page.has_previous()
    if has_previous:
        previous_page_number = page.previous_page_number()
    has_next = page.has_next()
    if has_next:
        next_page_number = page.next_page_number()

    return render_to_response('article/post_list.html', RequestContext(request, locals()))


def post_add(request):
    user_id = request.session["user_id"]
    if (user_id == None):
        return HttpResponseRedirect("/login")
    if (request.method == 'POST'):
        form = ArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post = Article(
                title=cd["title"],
                content=cd["content"],
                tags=cd["tags"],
                types=cd["types"],
                author=User(id=user_id)
            )
            post.save()
            return HttpResponseRedirect("/articles/%d" % post.id)
    else:
        form = ArticleForm()
    return render_to_response("article/post_edit.html", {'form': form},
                              context_instance=RequestContext(request))


def post_mod(request, id):
    user_id = request.session["user_id"]
    if user_id == None:
        return HttpResponseRedirect("/login")

    post = get_object_or_404(Article, pk=id)

    if post.author.id != user_id:
        return HttpResponse("权限不足")
    # post is modify
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            cd = form.cleaned_data
            post.title = cd["title"]
            post.content = cd["content"]
            post.tags = cd["tags"]
            post.types = cd["types"]
            post.save()
            return HttpResponseRedirect("/postlist")
    else:
        form = ArticleForm(instance=post)
    return render_to_response("article/post_edit.html", {'form': form, 'id': id},
                              context_instance=RequestContext(request))


def post_del(request, id):
    user_id = request.session["user_id"]
    if user_id == None:
        return HttpResponseRedirect("/login")

    post = get_object_or_404(Article, pk=id)

    if post.author.id != user_id:
        return HttpResponse("权限不足")

    post.delete()
    return HttpResponseRedirect("/postlist")

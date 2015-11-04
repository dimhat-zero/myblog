from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from myblog.models import Article,User
from myblog.article.forms import ArticleForm
from django.template import RequestContext


def article_detail(request,id):
	if request.method == 'POST':
		#update form
		pass
	elif request.method == 'GET':
		try:
			article = Article.objects.get(id=id)
		except Article.DoesNotExist:
			raise Http404
		else:
			pass
		return render_to_response('article/article_detail.html',{'article':article})
	else:
		raise Http404

def post_article(request):
	if(request.method=='POST'):
		form = ArticleForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			article = Article(
				title=cd["title"],
				content=cd["content"],
				tags=cd["tags"],
				types=cd["types"],
				author=User(id=request.session["user_id"])
			)
			article.save()
			return HttpResponseRedirect("/article/%d" % article.id)
	else:
		form = ArticleForm()
	return render_to_response("article/post_article.html",{'form':form},
                              context_instance=RequestContext(request))


		
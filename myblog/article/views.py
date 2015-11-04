from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from myblog.models import Article


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
		
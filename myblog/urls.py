"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

# myblog
urlpatterns += patterns('myblog.views',
	(r'^$','index'),
	(r'^hello/$','hello'),
    (r'^manage$','manage'),
)

# user
urlpatterns += patterns('myblog.user.views',
	(r'^register$','register'),
    (r'^register_success$','register_success'),
    (r'^login$','login'),
    (r'^json$','test_json'),
)

# article
urlpatterns += patterns('myblog.article.views',
    (r'^article/(\d+)$','article_detail'),
)
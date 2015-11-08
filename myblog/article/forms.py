# -*- coding: UTF-8 -*-
from django import forms
from myblog.models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField(max_length=100, required=False)
    types = forms.CharField(max_length=20)

    class Meta:
        model = Article
        fields = {'title','content','tags','types'}
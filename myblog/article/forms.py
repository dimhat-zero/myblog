from django import forms

class ArticleForm(forms.Form):
	title = forms.CharField(max_length=50)
	content = forms.CharField(widget=forms.Textarea)
	tags = forms.CharField(max_length=100,required=False)
	types = forms.CharField(max_length=20)
	

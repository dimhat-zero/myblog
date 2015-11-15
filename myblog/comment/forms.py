from django import forms
from myblog.models import Comment
class CommentForm(forms.ModelForm):
    comment_parent_id = forms.IntegerField(required=False)  # 外键
    user_id = forms.IntegerField(required=False)  # 发布人，没登录为空
    author = forms.CharField(max_length=50)
    email = forms.EmailField()
    content = forms.CharField(max_length=500)

    class Meta:
        model = Comment
        fields = {'author','email','content'}
        #fields = '__all__'
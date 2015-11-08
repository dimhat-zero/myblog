# -*- coding: UTF-8 -*-
from django import forms
from myblog.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3,max_length=30)
    password = forms.CharField(min_length=3,max_length=30)
    email = forms.EmailField()
    my_code = forms.CharField(min_length=4, max_length=6)

    # http://segmentfault.com/q/1010000002470490
    # https://stackoverflow.com/questions/27821252/django-form-field-validation-and-error-display
    # clean_field校验
    def clean_my_code(self):
        my_code = self.cleaned_data['my_code']
        if my_code != 'guess':
            raise forms.validationError("code is error")  # 邀请码不正确！
        return my_code


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class ModifyForm(forms.ModelForm):
    nickname = forms.CharField(max_length=30)
    email = forms.EmailField(help_text="请输入您的邮箱")
    is_active = forms.TypedChoiceField(
        coerce=lambda x:x=='True',
        choices=((False,'否'),(True,'是')),
        widget=forms.RadioSelect
    )
    is_staff =  forms.TypedChoiceField(
        coerce=lambda x:x=='True',
        choices=((False,'否'),(True,'是')),
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields={'nickname','email','is_active','is_staff'}


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
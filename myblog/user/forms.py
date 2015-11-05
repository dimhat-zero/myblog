# -*- coding: UTF-8 -*-
from django import forms


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


class ModifyForm(forms.Form):
    password = forms.CharField(max_length=30)
    nickname = forms.CharField(max_length=30)
    email = forms.EmailField()
    is_active = forms.BooleanField()
    is_staff = forms.BooleanField()


class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    nickname = forms.CharField(max_length=30)
    email = forms.EmailField()
    register_date = forms.DateField()
    is_active = forms.BooleanField()
    is_staff = forms.BooleanField()
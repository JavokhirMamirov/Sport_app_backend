from django import forms
from django.db import models
from django.forms import fields
from .models import SportObject, ObjectType, Category, Images

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SportObjectForm(forms.ModelForm):
    class Meta:
        model = SportObject
        fields = '__all__'

class ObjectTypeForm(forms.ModelForm):
    class Meta:
        model = ObjectType
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'img']



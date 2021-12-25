from django.db import models
from django.forms import fields
from django import forms
from sport.models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['full_name', 'object_name', 'address', 'phone', 'email', 'is_active']
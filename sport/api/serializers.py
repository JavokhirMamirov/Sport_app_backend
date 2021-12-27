from django.db import models
from django.db.models import fields
from rest_framework import serializers

from sport.models import Category, SportObject, Orders


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportObject
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['full_name', 'object_name', 'address', 'phone', 'email']
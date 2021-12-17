from django.db.models import fields
from rest_framework import serializers
from sport.models import *

class SportObjectSerialier(serializers.ModelSerializer):
    class Meta:
        model = SportObject
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class objectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectType
        fields = ('name',)
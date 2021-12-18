from rest_framework import serializers

from sport.models import Category, SportObject


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportObject
        fields = '__all__'
from rest_framework import serializers

from sport.models import Category, SportObject, Orders, Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ObjectSerializer(serializers.ModelSerializer):

    images = ImagesSerializer(many=True, read_only=True)
    class Meta:
        model = SportObject
        fields = "__all__"

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['full_name', 'object_name', 'address', 'phone', 'email']
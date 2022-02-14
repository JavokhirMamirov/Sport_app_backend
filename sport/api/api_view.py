from rest_framework.decorators import api_view
from rest_framework.exceptions import server_error
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from sport.api.serializers import CategorySerializer, ObjectSerializer, OrdersSerializer
from sport.models import Category, Orders, SportObject
from rest_framework import generics


@api_view(['GET'])
def get_categories(request):
    try:
        categories = Category.objects.all()
        ser = CategorySerializer(categories, many=True)
        data = {
            "success": True,
            "data": ser.data
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f'{err}'
        }
    return Response(data)


@api_view(['GET'])
def get_objects(request):
    try:
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        object = SportObject.objects.filter(lat__gt=lat, lng__gt=lng).order_by('-lat', '-lng')
        serializer = ObjectSerializer(object, many=True)
        data = {
            "success": True,
            "data": serializer.data[0:10]
        }
    except Exception as err:
        data = {
            "success": False,
            "error": err
        }
    return Response(data)


class ProductList(generics.ListAPIView):
    queryset = SportObject.objects.all()
    serializer_class = ObjectSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category']
    search_fields = ('name', 'address',)

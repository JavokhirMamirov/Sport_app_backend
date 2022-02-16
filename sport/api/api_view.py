from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  SearchFilter
from sport.api.serializers import CategorySerializer, ObjectSerializer
from sport.models import Category, SportObject
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@api_view(["GET"])
def login(request):
    try:
        username = request.GET.get('phone')
        password = request.GET.get('password')
        user = User.objects.get(username=username)
        print(user.password)
        if user.check_password(password):
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            data = {
                "success": True,
                "data": {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone": user.username,
                    "token": token.key
                }
            }
        else:
            data = {
                "success": False,
                "error": "Login parol xato!"
            }

    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)

@api_view(['POST'])
def register(request):
    try:
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        username = request.data.get('phone')
        password = request.data.get('password')
        user = User.objects.create(
            username=username, first_name=first_name, last_name=last_name
        )
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        data = {
            "success": True,
            "data": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone": user.username,
                "token": token.key
            }
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)

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
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category']
    search_fields = ('name', 'address',)

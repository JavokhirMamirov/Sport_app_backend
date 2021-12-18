from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from sport.models import  SportObject
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

@api_view(["GET"])
def SportObjectListApiView(request):
    centers = SportObject.objects.all()
    search = request.GET.get("search")
    if search:
        centers = SportObject.objects.filter(Q(name__icontains=search) | Q(address__icontains=search))
    paginator = PageNumberPagination()
    paginator.page_size = 1
    result_page = paginator.paginate_queryset(centers, request)
    serializer = SportObjectSerialier(result_page, many = True)
    return paginator.get_paginated_response(serializer.data)



class SportObjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = SportObject.objects.all()
    serializer_class = SportObjectSerialier
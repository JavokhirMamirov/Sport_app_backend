from django.urls import path

from sport.api.api_view import get_categories, get_objects, ProductList

urlpatterns = [
    path('get-categories/', get_categories),
    path('get-objects/', get_objects),
    path('get-objects-list/', ProductList.as_view())
]
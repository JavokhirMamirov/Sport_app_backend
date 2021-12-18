from django.urls import path

from sport.api.api_view import get_categories

urlpatterns = [
    path('get-categories/', get_categories)
]
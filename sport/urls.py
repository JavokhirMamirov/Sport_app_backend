from django.urls import path

from sport.views import HomeView, ObjectsView, AddNewObjectView, ObjectDetailView, login

urlpatterns = [
    path('', HomeView, name="home"),
    path('sport-object/', ObjectsView, name="sport-object"),
    path('add-sport-object/', AddNewObjectView, name="add-sport-object"),
    path('sport-object-detail/', ObjectDetailView, name="sport-object-detail"),
    path('login/', login, name="login"),
]
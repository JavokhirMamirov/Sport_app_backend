from django.contrib.auth import logout
from django.urls import path

from sport.views import HomeView, ObjectsView, AddNewObjectView, ObjectDetailView, UpdateObjectView, login_view, \
    AddTypeUsers, \
    AddObjectCategory, CreateObject, DeleteObjectView, UpdateObject, add_image, delete_image

urlpatterns = [
    path('', HomeView, name="home"),
    path('sport-object/', ObjectsView, name="sport-object"),
    path('update-object/<int:pk>/', UpdateObjectView, name="update-object"),
    path('add-sport-object/', AddNewObjectView, name="add-sport-object"),
    path('sport-object-detail/<int:pk>/', ObjectDetailView, name="sport-object-detail"),
    path('login/', login_view, name="login"),
    path('logout/', logout, name="logout"),
    # action
    path('add-type-users', AddTypeUsers, name='add-type-url'),
    path('add-category-users', AddObjectCategory, name='add-category-url'),
    path('create-object', CreateObject, name='create-object'),
    path('delete-object', DeleteObjectView, name='delete-object'),
    path('update-object-post/<int:id>/', UpdateObject, name='update-object-post'),
    path('add-image', add_image, name="add_image"),
    path('delete-image', delete_image, name='delete_image')
]

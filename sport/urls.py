from django.urls import path,include

from sport.views import *

urlpatterns = [
    path('', HomeView, name="home"),
    path('api/',include('sport.api.urls')),
    path('sport-object/', ObjectsView, name="sport-object"),
    path('update-object/<int:pk>/', UpdateObjectView, name="update-object"),
    path('add-sport-object/', AddNewObjectView, name="add-sport-object"),
    path('sport-object-detail/<int:pk>/', ObjectDetailView, name="sport-object-detail"),
    path('login/', login_view, name="login"),
    path('sign-up', user_create, name='sign-up-url'),
    path('logout/', user_logout, name="logout"),
    ## action
    path('add-type-users', AddTypeUsers, name='add-type-url'),
    path('add-category-users', AddObjectCategory, name='add-category-url'),
    path('create-object', CreateObject, name='create-object'),
    path('delete-object', DeleteObjectView, name='delete-object'),
    path('update-object-post/<int:id>/', UpdateObject, name='update-object-post'),
    path('add-image', add_image, name="add_image"),
    path('delete-image', delete_image, name='delete_image'),
    path('add_user_info', add_info_user, name='user_info'),
    # error
    path('404', notf),
    path('500', server),
    # order
    path('order-new/', order_new, name='order-new-url'),
    path('order-accepted/', order_accepted, name='order-accepted-url'),
    path('order-not-accepted/', order_not_accepted, name='order-not-accepted-url'),
    path('delete-order/', delete_order, name='delete-order-url'),
    path('change-order/<int:pk>/', change_order, name='change-order-url'),
]
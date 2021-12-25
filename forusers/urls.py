from django.urls import path
from .views import Index, ListObjects, ObjectDetail, OrderSave

urlpatterns = [
    path('', Index, name='index_url'),
    path('objects/', ListObjects, name='objects_url'),
    path('object-detail/<int:pk>/', ObjectDetail, name='detail_url'),
    path('order-save/', OrderSave, name='order_save_url'),
]

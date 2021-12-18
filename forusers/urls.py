from django.urls import  path
from .views import Index, ListObjects, ObjectDetail


urlpatterns=[
    path('',Index, name='index_url'),
    path('object/',ListObjects, name='objects_url'),
    path('detail/',ObjectDetail, name='detail_url')
]
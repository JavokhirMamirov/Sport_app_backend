from django.urls import path
from  .views import SportObjectDetailView, SportObjectListApiView

urlpatterns = [
    path('object-list/', SportObjectListApiView),
    path('sport-object/<int:pk>/', SportObjectDetailView.as_view()),
]
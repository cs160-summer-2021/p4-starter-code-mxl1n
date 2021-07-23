# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('large/', views.large, name='large'),
    path('small/', views.small, name='small'),
    # path('<str:room_name>/', views.room, name='room')

]

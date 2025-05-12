from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_vocabulary, name='create_vocabulary'),
    path('list/', views.list_vocabulary, name='list_vocabulary')
]
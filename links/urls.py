from django.urls import path
from . import views

urlpatterns = [
    path('', views.link_list, name='link_list'),
    path('create/', views.link_create, name='link_create'),
    path('delete/<int:pk>/', views.link_delete, name='link_delete'),
]

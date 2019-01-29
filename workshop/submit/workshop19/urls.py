from django.urls import path
from . import views

urlpatterns = [
    path('students/<int:id>/', views.detail),
    path('students/', views.index),
    path('students/in_content/', views.in_content),
    path('out_content', views.out_content),
]
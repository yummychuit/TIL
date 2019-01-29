from django.urls import path
from . import views

urlpatterns = [
    path('info/', view.ssafy),
    path('student/<name>/', view.student),
]
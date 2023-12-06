from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('', views.getData),
path('post/', views.postData),
path('task/', views.getTask),
path('task/post/', views.postTask),
path('photo/', views.getPhoto),
path('photo/post/', views.postPhoto),
]
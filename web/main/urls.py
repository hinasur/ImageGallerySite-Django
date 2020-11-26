from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('post/<int:pk>/', views.post_detail, name='post_detail'),
  path('imagegallery/', views.image_list, name='image_list'),
  path('imagegallery/<int:pk>/', views.image_detail, name='image_detail'),
  path('imagegallery/new/', views.image_new, name='image_new'),
]
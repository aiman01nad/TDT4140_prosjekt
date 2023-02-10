from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
]
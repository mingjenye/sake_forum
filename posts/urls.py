from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('create/', views.post_create, name='post_create'),
]

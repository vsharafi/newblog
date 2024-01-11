from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.PostListView, name='posts_list' ),
    path('<int:pk>/', views.PostDetailView, name='post_detail')
]
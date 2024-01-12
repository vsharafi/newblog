from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.PostListView, name='posts_list' ),
    path('<int:pk>/', views.PostDetailView, name='post_detail'),
    path('add/', views.PostCreateView, name="post_add"),
    path('<int:pk>/update/', views.PostUpdateView, name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView, name='post_delete'),
]
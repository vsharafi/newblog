from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.PostListView.as_view(), name='posts_list' ),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('add/', views.PostCreateView.as_view(), name="post_add"),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
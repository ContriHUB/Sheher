from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView, 
    likes,
    dislikes,
    comment,
    your_posts
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('like/<int:Post_pk>', likes, name='like'),
    path('dislike/<int:Post_pk>', dislikes, name='dislike'),
    path('comment/<int:post_pk>', comment, name='comment'),
    path('your_post', your_posts, name='your_posts')
]
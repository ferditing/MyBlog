from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Home page that lists all posts
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/add/', views.add_post, name='add_post'),  # Add post
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'), 
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('manage/', views.manage_posts, name='manage_posts'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Home page that lists all posts
]

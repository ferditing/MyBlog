from django.shortcuts import render,  get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Retrieve all posts, ordered by newest first
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Fetch the post by ID or show a 404 if not found
    return render(request, 'blog/post_detail.html', {'post': post})
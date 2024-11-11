from django.shortcuts import render, redirect,  get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Retrieve all posts, ordered by newest first
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Fetch the post by ID or show a 404 if not found
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the post list after saving
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

# View to edit an existing post
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)  # Redirect to the post detail page
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        post.delete()
        return redirect('post_list')  # Redirect to post list after deletion
    
    return render(request, 'blog/delete_post.html', {'post': post})

@login_required
def manage_posts(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts ordered by latest
    return render(request, 'blog/manage_posts.html', {'posts': posts})

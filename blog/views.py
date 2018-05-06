from django.shortcuts import render, get_object_or_404

from .models import Post

def blog(request):
    posts = Post.objects
    return render(request, 'blog/index.html', { 'posts': posts })

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', { 'post': post })

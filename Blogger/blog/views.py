from django.shortcuts import render,redirect
from .models import Post
from django.utils import timezone

def home_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "blog/home.html", {"posts": posts})

def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(
            title=title,
            content=content,
            published_at=timezone.now()
        )

        return redirect("blog:home") 

    return render(request, "blog/add_post.html")

def manage_posts(request):
    posts = Post.objects.all().order_by("-published_at")
    return render(request, "blog/manage_posts.html", {"posts": posts})

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.is_published = bool(request.POST.get("is_published"))

        post.save()
        return redirect("blog:manage_posts")

    return render(request, "blog/edit_post.html", {"post": post})
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("blog:manage_posts")

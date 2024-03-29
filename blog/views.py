from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Like, Dislike, Comment

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']


def postdetailview(request, post_pk):
    user = request.user
    post = Post.objects.get(pk=post_pk)
    all_comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        content = request.POST.get('comment')
        new_commment = Comment.objects.create(user=user, post=post,content=content)
        new_commment.save()
    context = {
        "post": post,
        "comments" : all_comments,
    }
    return render(request, "blog/post_detail.html", context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'picture', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'picture', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def likes(request, Post_pk):
    user = request.user
    post = Post.objects.get(pk=Post_pk)
    current_likes = Post.objects.get(pk=Post_pk).likes
    current_dislikes = Post.objects.get(pk=Post_pk).dislikes
    liked = Like.objects.filter(user=user, post=post)
    disliked = Dislike.objects.filter(user=user, post=post)
    if not liked and not disliked:

        liked = Like.objects.create(user=user, post=post)
        current_likes = current_likes + 1

    elif not liked and disliked:

        liked = Like.objects.create(user=user, post=post)
        disliked = Dislike.objects.filter(user=user, post=post).delete()
        current_likes = current_likes + 1
        current_dislikes = current_dislikes - 1

    else:

        liked = Like.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    Post.objects.filter(pk=Post_pk).update(likes=current_likes)
    Post.objects.filter(pk=Post_pk).update(dislikes=current_dislikes)
    return redirect('blog-home')

def dislikes(request, Post_pk):
    user = request.user
    post = Post.objects.get(pk=Post_pk)
    current_likes = Post.objects.get(pk=Post_pk).likes
    current_dislikes = Post.objects.get(pk=Post_pk).dislikes
    liked = Like.objects.filter(user=user, post=post)
    disliked = Dislike.objects.filter(user=user, post=post)
    if not disliked and not liked:

        disliked = Dislike.objects.create(user=user, post=post)
        current_dislikes = current_dislikes + 1

    elif not disliked and liked:

        disliked = Dislike.objects.create(user=user, post=post)
        liked = Like.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        current_dislikes = current_dislikes + 1

    else:

        disliked = Dislike.objects.filter(user=user, post=post).delete()
        current_dislikes = current_dislikes - 1

    Post.objects.filter(pk=Post_pk).update(likes=current_likes)
    Post.objects.filter(pk=Post_pk).update(dislikes=current_dislikes)
    return redirect('blog-home')

def your_posts(request):
    posts = Post.objects.filter(author_id=request.user.id).order_by('-date_posted')
    context = {
        "posts": posts
    }
    return render(request, 'blog/your_post.html', context)
    
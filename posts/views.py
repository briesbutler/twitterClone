from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from distutils.log import error
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

# Create your views here.

@ensure_csrf_cookie
def index(request, **post_id):
    if post_id != {}:
        val = next(iter(post_id.items()))[1]
        post = Post.objects.get(id=val)

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        posts = Post.objects.all().order_by('-id')[:20]
        return render(request, 'index.html')
    # newpost
    else:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                return error
        posts = Post.objects.all().order_by('-id')[:20]
        return render(request, 'index.html',
                      {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


@ensure_csrf_cookie
def editTweet(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    posts = Post.objects.all().order_by('-id')[:20]
    return render(request, 'index.html')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'edit.html', {'post': post, 'post_id': post_id})


@csrf_exempt
def tweetLikeAdd(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        like_count = post.like_count
        
        Post.objects.filter(id=post_id).update(like_count = like_count + 1)
        context = {'post_id': post_id, 'post': post}
    return render(request, 'index.html')


@csrf_exempt
def tweetLikeSubtract(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        like_count = post.like_count
        
        Post.objects.filter(id=post_id).update(like_count = like_count - 1)
        context = {'post_id': post_id, 'post': post}
    return render(request, 'index.html')

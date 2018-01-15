from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from videoapp.forms import PostCreateForm, CommentForm
from videoapp.models import Post
from videosite.storage_backends import CacheMediaStorage

def post_list(request):
    posts = Post.objects.filter(upload_date__lte=timezone.now()).order_by('upload_date')
    return render(request, 'media/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'media/post_detail.html', {'post': post})

@login_required
def post_new(request):
    template = 'media/post_edit.html'

    post_create_form = PostCreateForm()

    if request.method == 'POST':
        post_create_form = PostCreateForm(request.POST, request.FILES)

        if post_create_form.is_valid():
            video = request.FILES.get('video', None)

            if video:
                post_item = Post(video = video,
                                 video_cache = video)

                title = request.POST.get('title', None);
                description = request.POST.get('description', None);

                if title:
                    post_item.title = title
                if description:
                    post_item.description = description

                post_item.author = request.user
                post_item.upload_date = timezone.now()

                post_item.save()

                post_item.delete_cache()

                #media_item.video_mp4.generate()
                #media_item.video_ogg.generate()

                return HttpResponseRedirect(reverse('post_list'))

    context = {
        'form' : post_create_form
    }

    return render(request, template, context)

@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostCreateForm(instance=post)
    return render(request, 'media/post_edit.html', {'form': form})

@login_required
def add_comment_to_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'media/add_comment_to_post.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            posts = Post.objects.filter(upload_date__lte=timezone.now()).order_by('upload_date')
            return render(request, 'media/post_list.html', {'posts': posts})
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user).order_by('upload_date')
    return render(request, 'media/account.html', {'posts': posts})
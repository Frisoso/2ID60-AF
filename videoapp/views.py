from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from videoapp.forms import PostCreateForm
from videoapp.models import Post

def post_list(request):
    posts = Post.objects.filter(upload_date__lte=timezone.now()).order_by('upload_date')
    return render(request, 'media/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
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
                post_item = MediaItem(video = video)
                post_item.author = request.user
                post_item.upload_date = timezone.now()

                post_item.save()

                #media_item.video_mp4.generate()
                #media_item.video_ogg.generate()

                return HttpResponseRedirect(reverse('post_list'))

    context = {
        'item_create_form' : post_create_form,
    }

    return render(request, template, context)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
            return render(request, 'media/post_list.html', {'posts': posts})
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def list(request):
    template = 'media/list.html'

    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }

    return render(request, template, context)

def item_create(request):
    template = 'media/item_create.html'

    post_create_form = PostCreateForm()

    if request.method == 'POST':
        post_create_form = PostCreateForm(request.POST, request.FILES)

        if post_create_form.is_valid():
            video = request.FILES.get('video', None)

            if video:
                media_item = MediaItem(video = video)
                media_item.save()

                #media_item.video_mp4.generate()
                #media_item.video_ogg.generate()

                return HttpResponseRedirect(reverse('list'))

    context = {
        'post_create_form' : post_create_form,
    }

    return render(request, template, context)

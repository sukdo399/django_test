import os
import logging

from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from .ExcelParser import ExcelParser

logger = logging.getLogger('logger')

@login_required
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'data_app/post_list.html', {'posts': posts})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'data_app/post_detail.html', {'post': post})


@login_required
def post_error(request, err):
    logger.error(err)
    return render(request, 'data_app/post_error.html', {'err': err})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            logger.debug("request.FILES['file']: %s" % request.FILES['file'])
            try:
                ExcelParser.get_data(request.FILES['file'])
            except NameError as e:
                logger.error(e.args[0])
                return redirect('post_error', err=e.args[0])

            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'data_app/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'data_app/post_edit.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    os.remove(str(post.file))
    post.delete()

    return redirect('post_list')

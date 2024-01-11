from django.shortcuts import render, get_object_or_404
from .models import Post


def PostListView(request):
    posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
    return render(request, 'blog/posts_list.html', {'posts':posts} )


def PostDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

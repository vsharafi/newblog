from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm



def PostListView(request):
    posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
    return render(request, 'blog/posts_list.html', {'posts':posts} )


def PostDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def PostCreateView(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_add.html', {'form': form})


def PostUpdateView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post )
    if form.is_valid() and form.has_changed():
        form.save()
        return redirect('post_detail', pk=post.id)
    return render(request, 'blog/post_add.html', {'form':form})


def PostDeleteView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('posts_list')
    return render(request, 'blog/post_delete.html', {'post':post})
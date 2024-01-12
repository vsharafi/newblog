from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import Post
from .forms import PostForm
from django.views import generic






class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')
    

# def PostListView(request):
#     posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts':posts} )


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'

# def PostDetailView(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
    

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_add.html'
    # def get_success_url(self):
    #     return reverse('post_detail', args=[self.object.pk])



# def PostCreateView(request):
    
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_add.html', {'form': form})


class PostUpdateView(generic.UpdateView):
    form_class = PostForm
    template_name = 'blog/post_add.html'
    model = Post

    def form_valid(self, form):
        if form.has_changed():
            form.save()
            return redirect('post_detail', self.object.pk)
        else:
            return redirect('post_update', self.object.pk)

# def PostUpdateView(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post )
#     if form.is_valid() and form.has_changed():
#         form.save()
#         return redirect('post_detail', pk=post.id)
#     return render(request, 'blog/post_add.html', {'form':form})
        
class PostDeleteView(generic.DeleteView):
    template_name = 'blog/post_delete.html'
    model = Post
    # success_url = reverse_lazy('posts_list')

    def get_success_url(self):
        return reverse('posts_list')

# def PostDeleteView(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', {'post':post})
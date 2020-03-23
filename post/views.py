from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .models import Post


@login_required()
def new_post(request):
    return render(request, 'post/new_post.html')


@method_decorator(login_required, name='get')
class PostList(ListView):
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'post_list'


@method_decorator(login_required, name='get')
class PostDetail(DetailView):
    model = Post
    template_name = 'post/post.html'
    pk_url_kwarg = 'pk'

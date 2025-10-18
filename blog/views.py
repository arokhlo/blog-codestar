from django.shortcuts import render
from .models import Post
from django.views import generic

class PostList(generic.ListView):       
    queryset = Post.objects.all
    template_name = 'post_list.html'
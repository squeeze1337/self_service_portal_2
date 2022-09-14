from django.shortcuts import render
from django.views.generic import CreateView, ListView

from self_service_portal.posts.models import Post, PostCategory


# Create your views here.
class PostCreateView(CreateView):
    model = Post
    fields = ["status", "title", "sub_title", "category", "conten", "image"]


class PostCategoryCreateView(CreateView):
    model = PostCategory
    fields = ["title", "description"]


class PostListView(ListView):
    mode = Post
    queryset = Post.objects.published()

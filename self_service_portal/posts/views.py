from django.shortcuts import render
from django.views.generic import CreateView

from self_service_portal.posts.models import Post


# Create your views here.
class PostCreateView(CreateView):
    model = Post
    fields = ["status", "title", "sub_title"]

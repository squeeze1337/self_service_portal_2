from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, View

from self_service_portal.posts.forms import PostCreateForm
from self_service_portal.posts.models import Post, PostCategory


# Create your views here.
class PostDetailView(View):
    def get(self. request, *args, **kwargs):
        pass


class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    success_message = _("Blog Post erfolgreich erstellt.")


class PostCategoryCreateView(CreateView):
    model = PostCategory
    fields = ["title", "description"]


class PostListView(ListView):
    mode = Post
    queryset = Post.objects.published()

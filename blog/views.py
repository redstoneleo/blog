from django.views import generic
from .models import *


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/blog_index_page.html"
    context_object_name = "postList"

class CategoryView(generic.ListView):
    model = Post
    template_name = "blog/blog_index_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["postList"] = Post.objects.filter(category=self.kwargs['category'])
        return context

class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/blog_page.html"
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Post

# Create your views here.
# def home(request):
#     return render(request, 'blog/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

class PostDetail(DetailView):
    model = Post 
    template_name = 'blog/post_detail.html'


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'
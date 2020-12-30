from typing import List
from django.shortcuts import render
from .models import Post, Picture, Category
from django.core.paginator import Paginator
from django.views import generic
from django.views.generic import ListView


def base(request):
    return render(request, 'core/base.html')


def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'core/home.html', {'posts': posts})
    

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_date')
    template_name = 'home.html'


def post_detail(request, slug=None):
    post = Post.objects.get(slug=slug)
    return render(request, 'core/post_detail.html', {'post':post})


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def base_gallery(request):
    pictures = Picture.objects.all()
    paginator = Paginator(pictures, 16)
    page = request.GET.get('page')
    pictures = paginator.get_page(page)
    return render(request, 'core/base_gallery.html', {'pictures': pictures})
    
    
class PictureList(generic.ListView):
    queryset = Picture.objects.all().order_by('-created_date')
    template_name = 'base_gallery.html'


def contact(request):
    return render(request, 'core/contact.html', {'contact': contact})


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'
    
    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']),
        }
        return content


def category_list(request):
    category_list_GS = Category.objects.exclude(name='default').filter(kind='GS')
    category_list_DIY = Category.objects.exclude(name='default').filter(kind='DIY')
    category_list_GR = Category.objects.exclude(name='default').filter(kind='GR')
    category_list_TR = Category.objects.exclude(name='default').filter(kind='TR')
    context = {
        "category_list_GS": category_list_GS,
        "category_list_DIY": category_list_DIY,
        "category_list_GR": category_list_GR,
        "category_list_TR": category_list_TR,
        
    }
    return context
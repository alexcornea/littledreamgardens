from django.shortcuts import render
from .models import Post, Picture
from django.core.paginator import Paginator
from django.views import generic


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
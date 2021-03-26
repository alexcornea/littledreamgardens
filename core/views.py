from core.forms import CommentForm, PostSearchForm, ContactForm
from typing import List
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Category, Picture, Post


def base(request):
    return render(request, "core/base.html")


def home(request):
    posts = Post.objects.all().order_by('-created_date')
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request, "core/home.html", {"posts": posts})



class PostList(generic.ListView):
    model = Post
    template_name = "home.html"


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            
            # Create comment object but don't save database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request, "core/post_detail.html", {"post": post,
                                                     "comments": comments,
                                                     "new_comment": new_comment,
                                                     "comment_form": comment_form})


class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"


def base_gallery(request):
    pictures = Picture.objects.all()
    paginator = Paginator(pictures, 16)
    page = request.GET.get("page")
    pictures = paginator.get_page(page)
    return render(request, "core/base_gallery.html", {"pictures": pictures})


class PictureList(generic.ListView):
    queryset = Picture.objects.all().order_by("-created_date")
    template_name = "base_gallery.html"


def contact(request):
    return render(request, "core/contact.html", {"contact": contact})


class CatListView(ListView):
    template_name = "category.html"
    context_object_name = "catlist"
    posts = Post.objects.all().order_by('-created_date')

    def get_queryset(self):
        content = {
            "cat": self.kwargs["category"],
            "posts": Post.objects.filter(category__name=self.kwargs["category"]).order_by('created_date'),
        }
        return content
        



def category_list(request):
    category_list_GS = Category.objects.exclude(name="default").filter(kind="GS")
    category_list_DIY = Category.objects.exclude(name="default").filter(kind="DIY")
    category_list_GR = Category.objects.exclude(name="default").filter(kind="GR")
    category_list_TR = Category.objects.exclude(name="default").filter(kind="TR")
    context = {
        "category_list_GS": category_list_GS,
        "category_list_DIY": category_list_DIY,
        "category_list_GR": category_list_GR,
        "category_list_TR": category_list_TR,
    }
    return context
    
    
def post_search(request):
    form = PostSearchForm()
    q = ''
    results = []
    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Post.objects.filter(title__contains=q)
    return render(request, "search.html", 
                    {'form': form,
                     'q': q,
                     'results': results, })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            
            try: 
                send_mail(subject, message, 'email', ['broncecilla@hotmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("home")

    form = ContactForm()
    return render(request, "core/contact.html", {'form':form})
                
            
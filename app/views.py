from django.core.paginator import Paginator
from django.shortcuts import render
from .models import BlogPost

def index(request):
    posts_list = BlogPost.objects.filter(status='published')
    paginator = Paginator(posts_list, 10)  # Affiche 10 articles par page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'app/index.html', {'posts': posts})


def detail(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    return render(request, 'app/detail.html', {'post': post})


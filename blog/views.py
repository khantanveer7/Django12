from django.http import HttpResponse, request
from home.models import Blog
from django.shortcuts import render
import math


# Create your views here.

# def blog(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def blog(request):
    no_of_post = 4
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)

    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_post: page * no_of_post]
    if page > 1:
        prev = page - 1
    else:
        prev = None
    if page < math.ceil(length / no_of_post):
        nxt = page + 1
    else:
        nxt = None

    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'blog.html', context)


def post(request, slug):
    blogs = Blog.objects.filter(slug=slug).first()
    context = {'blogs': blogs, }
    return render(request, 'post.html', context)

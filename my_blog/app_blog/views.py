from django.shortcuts import render
from app_blog.models import Post, PostCategory, Quote


def index(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all(),
        'categories': PostCategory.objects.all(),
        'quotes': Quote.objects.all()
    }

    return render(request, 'app_blog/index.html', context)


def about(request):
    context = {'title': 'About'}
    return render(request, 'app_blog/about.html', context)


def styles(request):
    context = {'title': 'Styles'}
    return render(request, 'app_blog/styles.html', context)


def contact(request):
    context = {'title': 'Contact'}
    return render(request, 'app_blog/contact.html', context)

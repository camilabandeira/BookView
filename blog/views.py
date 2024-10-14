from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def homepage(request):
    posts = Post.objects.order_by('-created_on')
    
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/homepage.html', {'page_obj': page_obj})

def reviews_page(request):
    # Fetch all posts, ordered by latest
    posts = Post.objects.order_by('-created_on')

    # Paginate: 6 posts per page for the reviews page
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/reviews_page.html', {'page_obj': page_obj})

def about_page(request):
    return render(request, 'blog/about_page.html')


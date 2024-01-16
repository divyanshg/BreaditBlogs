from django.shortcuts import render
from .models import Category, Blog

# Create your views here.
def index(request):
    #Fetchin required data
    categories = Category.objects.all()
    latest_posts = Blog.objects.all().order_by('-pub_date')[:8]
    featured_posts = Blog.objects.all()[:5]

    #Preparing data to be sent to template
    data = {
        "categories": categories,
        "latest_posts":  latest_posts,
        "featured_posts": featured_posts
    }

    #Renderig template and Sending data to template
    return render(request, 'index.html', data)

def blog_detail(request, blog_id):
    #Fetching required data
    blog = Blog.objects.get(slug=blog_id)

    #Preparing data to be sent to template
    data = {
        "blog": blog
    }

    #Renderig template and Sending data to template
    return render(request, 'blog.html', data)
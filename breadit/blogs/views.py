from django.shortcuts import render
from .models import Category, Blog, Subscription

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

def contact(request):
    return render(request, 'contact.html')

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
def check(email):
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")

def newsletter(request):
    if(request.method != "POST"):
        return render(request, 'newsletter.html', {})


    email = request.POST.get('email')
    if(email == None):
        return render(request, 'newsletter.html', {
            "error": "Please enter a valid email address.",
            "success": "False"
        })
    elif checkEmail(email) == False:
        return render(request, 'newsletter.html', {
            "error": "Please enter a valid email address.",
            "success": "False",
            "email": email
        })

    #check if email already exists
    try:
        Subscription.objects.get(email=email)
        return render(request, 'newsletter.html', {
            "error": "You have already subscribed to our newsletter.",
            "email": email,
            "success": "False"
        })
    except:
        pass
    
    subscriptions = Subscription(email=email)
    subscriptions.save()

    return render(request, 'newsletter.html', {
        "message": "You have successfully subscribed to our newsletter.",
        "success": "True"
    })

def addBlog(request):
    if(request.method == "POST"):
        return render(request, "newBlog.html")
    else:
        return render(request, "newBlog.html")
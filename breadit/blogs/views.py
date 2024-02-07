from django.shortcuts import render, redirect
from .models import Category, Blog, Subscription, User, Comment

def isAuthenticated(request):
    if 'user' in request.session:
        return True
    else:
        return False

# Create your views here.
def index(request):
    #Fetching required data
    categories = Category.objects.all()
    latest_posts = Blog.objects.all().order_by('-pub_date')[:8]
    featured_posts = Blog.objects.all()[:5]

    #Preparing data to be sent to template
    data = {
        "categories": categories,
        "latest_posts":  latest_posts,
        "featured_posts": featured_posts,
        "isAuthenticated": isAuthenticated(request)
    }

    #Renderig template and Sending data to template
    return render(request, 'index.html', data)

def blog_detail(request, blog_id):
    #Fetching required data
    blog = Blog.objects.get(slug=blog_id)
    blog.views += 1
    blog.save()

    comments = Comment.objects.filter(blog=blog)
    #Preparing data to be sent to template
    data = {
        "blog": blog,
        "isAuthenticated": isAuthenticated(request),
        "comments": comments
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

def category(request):
    category = request.GET.get('q')

    if(category == None):
        return render(request, 'category.html', {
            "error": "Please select a category.",
        "isAuthenticated": isAuthenticated(request)
        })

    blogs = Blog.objects.filter(category__name=category)


    return render(request, 'category.html', {
        "blogs": blogs,
        "category": category,
        "isAuthenticated": isAuthenticated(request)
    })

def likeBlog(request):
    if not isAuthenticated(request):
        return redirect('/auth/login')

    blog_id = request.GET.get('blog_id')
    blog = Blog.objects.get(slug=blog_id)
    blog.likesCount += 1
    blog.save()

    # goback
    return redirect(request.META.get('HTTP_REFERER'))


#auth views
def login(request):
    if isAuthenticated(request):
        return redirect('/')
    
    if request.method == "GET":
        return render(request, 'auth/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
            request.session['user'] = user.email
            return redirect('/')
        except:
            return render(request, 'auth/login.html', {
                "error": "Invalid email or password."
            })

def register(request):
    if isAuthenticated(request):
        return redirect('/')

    if request.method == "GET":
        return render(request, 'auth/register.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #check if email already exists
        try:
            User.objects.get(email=email)
            return render(request, 'auth/register.html', {
                "error": "Email already exists."
            })
        except:
            pass

        user = User(email=email, password=password)
        user.save()

        return render(request, 'auth/register.html')

def addComment(request):
    if not isAuthenticated(request):
        return redirect('/auth/login')

    if request.method == "POST":
        blog_id = request.POST.get('blog_id')
        comment = request.POST.get('comment')

        blog = Blog.objects.get(slug=blog_id)
        user = User.objects.get(email=request.session['user'])

        comment = Comment(user=user, blog=blog, comment=comment)
        comment.save()

        blog.commentCount += 1  
        blog.save()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))

def deleteComment(request):
    if not isAuthenticated(request):
        return redirect('/auth/login')

    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))

def editComment(request):
    if not isAuthenticated(request):
        return redirect('/auth/login')
        
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        comment.comment = request.POST.get('comment')
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))

def logout(request):
    del request.session['user']
    return redirect('/')
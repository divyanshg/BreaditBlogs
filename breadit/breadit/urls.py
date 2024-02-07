from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blogs import views as blogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogViews.index, name='index'),
    path("blog/<str:blog_id>/", blogViews.blog_detail, name="blog_detail"),
    path("contact/", blogViews.contact, name="contact"),
    path("newsletter/", blogViews.newsletter, name="newsletter"),
    path("new-blog/", blogViews.addBlog, name="newBlog"),
    path("category", blogViews.category, name="category"),
    path("likeBlog/", blogViews.likeBlog, name="category"),
    path('auth/login/', blogViews.login, name='login'),
    path('auth/register/', blogViews.register, name='register'),
    path('auth/logout/', blogViews.logout, name='logout'),
    path('addComment/', blogViews.addComment, name='addComment'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
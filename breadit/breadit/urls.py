"""
URL configuration for breadit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("blog/<str:blog_id>/", views.blog_detail, name="blog_detail"),
    path("contact/", views.contact, name="contact"),
    path("newsletter/", views.newsletter, name="newsletter"),
    path("new-blog/", views.addBlog, name="newBlog"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
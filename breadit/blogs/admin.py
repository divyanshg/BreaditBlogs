from django.contrib import admin
from blogs.models import Author, Blog, Category, Subscription

# Register your models here.
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Subscription)

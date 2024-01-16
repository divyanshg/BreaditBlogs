from django.contrib import admin
from blogs.models import Author, Blog, Category

# Register your models here.
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Category)

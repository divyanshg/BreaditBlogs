from django.db import models
from django.contrib.auth.models import User
import uuid 
from ckeditor.fields import RichTextField 

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    content = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    thumbnail = models.ImageField(upload_to='images', default='images/default.png')
    isFeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
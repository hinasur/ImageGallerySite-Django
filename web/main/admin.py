from django.contrib import admin
from .models import Book
from .models import Post
from .models import PhotoImage,Review

# Register your models here.
admin.site.register(Book)
admin.site.register(Post)
admin.site.register(PhotoImage)
admin.site.register(Review)
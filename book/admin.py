from django.contrib import admin

from django.contrib import admin
from .models import Category
from .models import Book

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)




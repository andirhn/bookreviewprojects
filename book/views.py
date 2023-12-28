
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Category
from .models import Book

def home(request):
    categories = Category.objects.all()
    searchJudul = request.GET.get('judul')
    category_id = request.GET.get('category_id')
    if searchJudul:
        books = Book.objects.filter(title__icontains=searchJudul)
    elif category_id :
        books = Book.objects.filter(category_id=category_id)
    else:
        books = Book.objects.all()
    return render(request, 'home.html', {'searchJudul':searchJudul,'categories' : categories,'books' :books})

def about(request):
    About = request.GET.get('TentangHalamanBuku')
    return render(request,'about.html')

def detail(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    return render(request,'detail.html',{'book' : book})
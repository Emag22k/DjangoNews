from django.shortcuts import render
from .models import NewsCategory,News

# Create your views here.

def home_page(request):
    new = News.objects.all()
    categories = NewsCategory.objects.all()
    context={"new":new, "categories":categories}
    return render(request, 'home.html',context)

def news_page(request):
    return render(request, 'news.html',)

def category_page(request):
    return render(request, "category.html")



from django.shortcuts import render
from store.models import Product, Category

def home(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'categories': categories})
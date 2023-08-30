from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator


# Create your views here.
def store(request, category_slug=None):
    category = None
    products = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category).order_by('product_name')

        page = request.GET.get("page")
        paginator = Paginator(products, 1)
        product_page = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True).order_by('product_name')

        page = request.GET.get("page")
        paginator = Paginator(products, 3)
        product_page = paginator.get_page(page)
    categories = Category.objects.all()
    context = {"products": product_page, "categories": categories}
    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    context = {"product": product}

    return render(request, "store/product-detail.html", context)

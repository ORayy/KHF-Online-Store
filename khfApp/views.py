from django.shortcuts import get_object_or_404, render

from .models import Category, Product


# Create your views here.
# display data from Category Model to href in navbar
def categories(request):
    return {
        'categories': Category.objects.all()
    }

# display all data from Products Model to home.html
def all_products(request):
    products = Product.products.all()
    return render(request, 'khfApp/home.html', {'products': products})

# product detail page function
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'khfApp/product/single.html', {'product': product})

# product category page function
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'khfApp/product/category.html', {'category': category, 'products': products})
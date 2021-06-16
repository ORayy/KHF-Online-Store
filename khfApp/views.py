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
    products = Product.objects.all()
    return render(request, 'khfApp/home.html', {'products': products})

# product detail page function
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'khfApp/product/detail.html', {'product': product})

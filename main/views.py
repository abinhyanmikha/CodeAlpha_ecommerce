from django.shortcuts import render
from products.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'main/home.html', {'products': products})

def dashboard(request):
    total_products = Product.objects.count()
    return render(request, 'main/dashboard.html', {
        'total_products': total_products
    })

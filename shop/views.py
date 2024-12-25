from django.shortcuts import render
from django.http import HttpResponse


from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    products = Product.objects.filter(id=45500)
    print(products.first())
    print(products.last())
    print(products.exists())
    
    return render(request, 'shop/shop.html', {'products': products})

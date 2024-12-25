from django.shortcuts import render
from django.http import HttpResponse


from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.filter(inventory__lte=4)
    queryset = Product.objects.filter(inventory__lt=55)
    queryset = Product.objects.filter(inventory__gt=10)
    queryset = Product.objects.filter(inventory__gte=40)
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

from django.shortcuts import render
from django.http import HttpResponse


from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.filter(name__icontains='work')
    queryset = Product.objects.filter(name__contains='Work')

    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.filter(Q(inventory__lt=3) | Q(inventory__gt=95))
    queryset = Product.objects.filter(~Q(inventory__lt=50) | Q(name__startswith='s'))
    queryset = Product.objects.filter(~Q(inventory__lt=50) | Q(name__istartswith='s'))
    queryset = OrderItem.objects.filter(~Q(quantity__gt=8))
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

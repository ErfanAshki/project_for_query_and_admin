from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.defer('description', 'image', 'datetime_modified')
    queryset = Product.objects.only('id', 'name', 'inventory', 'unit_price')

    return render(request, 'shop/shop.html', {'products': list(queryset)})

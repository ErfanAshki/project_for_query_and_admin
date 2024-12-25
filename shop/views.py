from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.all().order_by('unit_price')
    queryset = Product.objects.filter(inventory__gt=90).order_by('-unit_price')
    queryset = Product.objects.all().order_by('inventory')
    queryset = Product.objects.all().order_by('inventory').reverse()

    return render(request, 'shop/shop.html', {'products': list(queryset)})

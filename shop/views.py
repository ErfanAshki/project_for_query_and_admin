from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.all().earliest('unit_price')
    queryset = Product.objects.all().latest('unit_price')

    return render(request, 'shop/shop.html')

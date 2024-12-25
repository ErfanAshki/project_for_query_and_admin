from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.all()[1:6]
    queryset = Product.objects.all()[ :50]
    queryset = Product.objects.all()[980 : ]

    return render(request, 'shop/shop.html', {'products': list(queryset)})

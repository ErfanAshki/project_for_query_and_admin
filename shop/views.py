from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = OrderItem.objects.filter(product_id=F('quantity'))
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

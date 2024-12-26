from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Order.objects.prefetch_related('items__product').select_related('customer').all()
    
    return render(request, 'shop/shop.html', {'orders': list(queryset)})

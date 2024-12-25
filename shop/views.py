from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = OrderItem.objects.filter(order_id=70).exclude(quantity__gt=10)
    queryset = Product.objects.filter(unit_price__lt=Decimal('780.5'))
    queryset = Order.objects.filter(customer__first_name__icontains='Kimberly')
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

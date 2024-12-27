from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value, Func, ExpressionWrapper, DecimalField

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Customer.objects.all().annotate(number_of_orders=Count('orders'))
    
    return render(request, 'shop/shop.html', {'order': list(queryset)})

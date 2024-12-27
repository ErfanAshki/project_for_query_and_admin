from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value, Func, ExpressionWrapper, DecimalField

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = OrderItem.objects.all().annotate(total_price=ExpressionWrapper(\
        F('unit_price') * F('quantity'), output_field=DecimalField()))
    
    queryset = OrderItem.objects.all().annotate(total_price=ExpressionWrapper(\
        F('unit_price') * 0.9, output_field=DecimalField()))
    
    return render(request, 'shop/shop.html', {'order': list(queryset)})

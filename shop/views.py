from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.aggregate(max_price=Max('unit_price'))
    queryset = Product.objects.aggregate(min_inventory=Min('inventory'))
    queryset = Product.objects.aggregate(sum_inventory=Sum('inventory'))
    
    return render(request, 'shop/shop.html', {'orders': list(queryset)})

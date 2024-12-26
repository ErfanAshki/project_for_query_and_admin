from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value, Func, ExpressionWrapper, DecimalField

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    # way one
    queryset = OrderItem.objects.values('order_id'). \
                    annotate(items_count=Count('order_id'))
    
    # way two
    queryset = Order.objects.all().annotate(items_count=Count('items'))
    
    return render(request, 'shop/shop.html', {'order': list(queryset)})

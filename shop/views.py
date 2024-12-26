from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.filter(inventory__gt=10).aggregate(number=Count('id'), avg_price=Avg('unit_price'))
    queryset = OrderItem.objects.filter(product_id=4599).aggregate(number=Count('id'))
    
    order_item_queryset = OrderItem.objects.values('product_id').distinct()
    queryset = Product.objects.filter(id__in=order_item_queryset).aggregate(number_of_product=Count('id'))

    return render(request, 'shop/shop.html', {'orders': list(queryset)})

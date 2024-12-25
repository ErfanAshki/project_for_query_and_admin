from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.values('id', 'name', 'inventory', 'datetime_created')
    queryset = Product.objects.values_list('id', 'name', 'inventory', 'datetime_created')
    queryset = Product.objects.values('id', 'name', 'inventory').order_by('-inventory')

    order_item_queryset = OrderItem.objects.values('product_id').distinct()
    queryset = Product.objects.filter(id__in=[order_item_queryset]).all()

    return render(request, 'shop/shop.html', {'products': list(queryset)})

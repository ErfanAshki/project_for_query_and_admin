from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.aggregate(Count('inventory'))
    queryset = Comment.objects.aggregate(Count('status'))
    queryset = OrderItem.objects.aggregate(Count('id'))
    queryset = OrderItem.objects.aggregate(Avg('quantity'))
    queryset = Product.objects.aggregate(Avg('inventory'))
    queryset = Product.objects.aggregate(Avg('unit_price'))
    queryset = Product.objects.aggregate(number_of_products=Count('inventory'))
    queryset = Product.objects.aggregate(average_of_price=Avg('unit_price'))
    
    return render(request, 'shop/shop.html', {'orders': list(queryset)})

from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    # queryset = Comment.objects.select_related('product').all()
    # return render(request, 'shop/shop.html', {'comments': list(queryset)})

    queryset = Product.objects.prefetch_related('comments').select_related('category').all()
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

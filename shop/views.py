from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value, Func, ExpressionWrapper, DecimalField

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), \
                                        function='CONCAT')).defer('first_name', 'last_name').all()
    
    return render(request, 'shop/shop.html', {'orders': list(queryset)})

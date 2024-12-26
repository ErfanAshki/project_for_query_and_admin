from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Category.objects.annotate(new_column=Value(55)).all()
    queryset = Category.objects.annotate(new_column=Value('sss')).all()
    queryset = Product.objects.annotate(price=F('unit_price')).all()
    queryset = OrderItem.objects.annotate(total_price=F('unit_price') * F('quantity')).all()
    
    return render(request, 'shop/shop.html', {'orders': list(queryset)})

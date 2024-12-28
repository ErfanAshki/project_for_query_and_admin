from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value, Func, ExpressionWrapper, DecimalField

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    OrderItem.objects.filter(id=170).delete()
    OrderItem.objects.filter(id=171).delete()
    OrderItem.objects.filter(id=172).delete()
    
    Order.objects.filter(id=93).delete()
    
    Product.objects.filter(id=5003).delete()
    Product.objects.filter(id=5004).delete()
    
    Category.objects.filter(id=701).delete()
    Category.objects.filter(id=702).delete()
    
    
    queryset = Category.objects.all().order_by('-id')
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

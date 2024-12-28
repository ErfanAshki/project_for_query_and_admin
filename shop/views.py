from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value, Func, ExpressionWrapper, DecimalField

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    order = Order()
    order.customer_id = 305
    order.save()
    
    # way one
    Order.objects.filter(id=91).delete()

    # way two
    order = Order(id=92)
    order.delete()
    
    queryset = Order.objects.all().order_by('-id')
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

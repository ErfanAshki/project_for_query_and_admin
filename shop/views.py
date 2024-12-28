from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value, Func, ExpressionWrapper, DecimalField
from django.db import transaction

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


# @transaction.atomic()
def some_view(request):
    with transaction.atomic():
        order = Order.objects.create(customer_id=311)

        order_item1 = OrderItem.objects.create(
            order=order,
            product_id=4500.
            quantity=5,
            unit_price=100
        )
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value, Func, ExpressionWrapper, DecimalField

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    # way one
    customer = Customer(id=303)
    customer.first_name = 'jenifer'
    customer.last_name = 'lopez'
    customer.phone_number = '625.451.4235x401'
    customer.birth_date = '2010-11-04'
    customer.email = 'jenifer@gmail.com'
    customer.save()
    
    queryset = Customer.objects.all().order_by('id')

    # way two
    customer = Customer.objects.get(id=304)
    customer.last_name = 'farangiiiii'
    customer.save()
    
    queryset = Customer.objects.all().order_by('id')
    
    # way three
    Customer.objects.filter(id=305).update(birth_date='2022-2-2')

    queryset = Customer.objects.all().order_by('id')

    return render(request, 'shop/shop.html', {'products': list(queryset)})

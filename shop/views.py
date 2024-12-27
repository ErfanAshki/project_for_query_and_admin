from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
from django.db.models import Q, F, Avg, Count, Max, Min, Sum, Value, Func, ExpressionWrapper, DecimalField

from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    # way one
    product = Product.objects.get(id=4500)
    customer = Customer.objects.get(id=310)
    
    Comment.objects.create(
        body='my comment',
        name=customer,
        product=product
    )
    
    # way two
    Comment.objects.create(
        body='my comment',
        name='erfan',
        product_id=4800
    )
    
    # way three
    product = Product.objects.get(id=4690)
    
    comment = Comment()
    comment.body = 'new comment for create'
    comment.name = 'pari'
    comment.product = product
    comment.save()
    
    queryset = Comment.objects.all().order_by('-id')
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

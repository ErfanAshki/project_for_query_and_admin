from django.shortcuts import render
from django.http import HttpResponse


from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.filter(name__icontains='work', datetime_created__year=2021, inventory__gt=5)
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

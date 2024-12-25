from django.shortcuts import render
from django.http import HttpResponse


from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.filter(datetime_created__year=2022)
    queryset = Product.objects.filter(datetime_created__month=10)
    queryset = Product.objects.filter(datetime_created__day=1)
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

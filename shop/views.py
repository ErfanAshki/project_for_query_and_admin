from django.shortcuts import render
from django.http import HttpResponse


from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Customer.objects.filter(birth_date__isnull=True)
    queryset = Customer.objects.filter(birth_date__isnull=False)

    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

from django.shortcuts import render
from django.http import HttpResponse


from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = Product.objects.filter(category__id=620)
    queryset = Product.objects.filter(category__title__icontains='think')
    queryset = Address.objects.filter(customer__first_name__icontains='jay')

    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

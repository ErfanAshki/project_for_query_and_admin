from django.shortcuts import render
from django.http import HttpResponse


from .models import Product, Discount, Category, Comment, Customer, Address, Cart, CartItem, Order, OrderItem


def some_view(request):
    queryset = OrderItem.objects.filter(product__id=4021)
    queryset = Product.objects.filter(inventory=50)
    queryset = Product.objects.filter(name__icontains='energy', inventory__gte=66)
    queryset = Order.objects.filter(status=Order.ORDER_STATUS_UNPAID)
    queryset = Order.objects.exclude(status=Order.ORDER_STATUS_UNPAID)
    
    return render(request, 'shop/shop.html', {'products': list(queryset)})

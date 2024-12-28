from django.contrib import admin

from .models import Product, Cart, CartItem, Category, Comment, Customer ,Order, OrderItem, Discount, Address


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'unit_price', 'inventory', 'datetime_created']
    ordering = ['id']
    list_per_page = 20    
    list_editable = ['unit_price', 'inventory']
    
    
admin.site.register(Product, ProductAdmin)

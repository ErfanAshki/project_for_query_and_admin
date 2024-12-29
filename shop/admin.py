from django.contrib import admin
from django.db.models import Count

from .models import Product, Cart, CartItem, Category, Comment, Customer ,Order, OrderItem, Discount, Address


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_title' , 'unit_price', 'inventory', 'inventory_status', 'datetime_created']
    ordering = ['id']
    list_per_page = 20    
    list_editable = ['unit_price', 'inventory']
    list_select_related = ['category']
    
    def inventory_status(self, product):
        if product.inventory < 10 :
            return 'LOW'
        elif product.inventory > 50 : 
            return 'HIGH'
        else:
            return 'MEDIUM'
        
    @admin.display(ordering='category__title')
    def category_title(self , product):
        return product.category.title
        
    
admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'datetime_created', 'number_of_items']
    ordering = ['id']
    list_per_page = 15    
    list_editable = ['status']
    
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('items'). \
            annotate(items_count=Count('items'))
    
    @admin.display(ordering='items_count')
    def number_of_items(self, order):
        return order.items_count
    
    
admin.site.register(Order, OrderAdmin)



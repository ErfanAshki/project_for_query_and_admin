from django.contrib import admin
from django.db.models import Count

from .models import Product, Cart, CartItem, Category, Comment, Customer ,Order, OrderItem, Discount, Address


class InventoryFilter(admin.SimpleListFilter):
    title = 'Critical Inventory Status'
    parameter_name = 'inventory'
    LESS_THAN_3 = '<3'
    BETWEEN_3_AND_10 = '3<=10'
    GREATER_THAN_10 = '>10'

    def lookups(self, request, model_admin):
        return [
            (InventoryFilter.LESS_THAN_3, 'High'),
            (InventoryFilter.BETWEEN_3_AND_10, 'Medium'),
            (InventoryFilter.GREATER_THAN_10, 'Ok')
        ]

    def queryset(self, request, queryset):
        if self.value() == InventoryFilter.LESS_THAN_3:
            return queryset.filter(inventory__lt=3)
        elif self.value() == InventoryFilter.BETWEEN_3_AND_10:
            return queryset.filter(inventory__range=(3, 10))
        elif self.value() == InventoryFilter.GREATER_THAN_10:
            return queryset.filter(inventory__gt=10)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_title' , 'unit_price', 'inventory', 'inventory_status', 'datetime_created']
    ordering = ['id']
    list_per_page = 20    
    list_editable = ['unit_price', 'inventory']
    list_select_related = ['category']
    list_filter = [InventoryFilter, 'category']
    search_fields = ['name__istartswith']
    list_display_links = ['id', 'name']
    
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


class ItemsFilter(admin.SimpleListFilter):
    title = 'Items Of Orders'
    parameter_name = 'items'
    LESS_THAN_3 = '<3'
    BETWEEN_3_AND_7 = '3<=7'
    GREATER_THAN_7 = '>7'

    def lookups(self, request, model_admin):
        return [
            (ItemsFilter.LESS_THAN_3, 'Ok'),
            (ItemsFilter.BETWEEN_3_AND_7, 'Normal'),
            (ItemsFilter.GREATER_THAN_7, 'Lot')
        ]

    def queryset(self, request, queryset):
        if self.value() == ItemsFilter.LESS_THAN_3:
            return queryset.filter(items_count__lt=3)
        elif self.value() == ItemsFilter.BETWEEN_3_AND_7:
            return queryset.filter(items_count__lte=7, items_count__gte=3)
        elif self.value() == ItemsFilter.GREATER_THAN_7:
            return queryset.filter(items_count__gt=7)
    
    def get_queryset(self):
        queryset = super(self).get_queryset().annotate(items_count=Count('items'))
        return queryset

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'datetime_created', 'number_of_items']
    ordering = ['id']
    list_per_page = 15    
    list_editable = ['status']
    list_filter = ['status', ItemsFilter]
    search_fields = ['customer__first_name', 'customer__last_name']
    list_display_links = ['id']
    
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('items'). \
            annotate(items_count=Count('items'))
    
    @admin.display(ordering='items_count')
    def number_of_items(self, order):
        return order.items_count
    
    
admin.site.register(Order, OrderAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name' , 'phone_number', 'birth_date', 'email']
    ordering = ['id']
    list_per_page = 20    
    list_editable = ['birth_date', 'email']
    list_filter = ['orders']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    list_display_links = ['id', 'first_name']
    
    
admin.site.register(Customer, CustomerAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'name' , 'status', 'datetime_created']
    ordering = ['id']
    list_per_page = 20    
    list_editable = ['status']
    list_select_related = ['product']
    list_filter = ['status']
    search_fields = ['product__name']
    list_display_links = ['id', 'product']
    
    
admin.site.register(Comment, CommentAdmin)


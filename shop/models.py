from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.utils import timezone
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    body = models.TextField(verbose_name=_('body'), blank=True)
    

class Discount(models.Model):
    discount = models.FloatField(verbose_name=_('discount'))
    description = models.TextField(verbose_name=_('description'))
    

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    slug = models.SlugField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_image', null=True, blank=True)
    inventory = models.PositiveSmallIntegerField()
    discount = models.ManyToManyField('Discount', blank=True)
    datetime_created = models.DateTimeField(default=timezone.now , verbose_name=_('date of created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('date of modified'))
    

class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first_name'))    
    last_name = models.CharField(max_length=100, verbose_name=_('last_name'))
    age = models.PositiveIntegerField(verbose_name=_('age'))
    birthdate = models.DateField(verbose_name=_('birthdate'))
    email = models.EmailField(verbose_name=_('email'), blank=True, null=True)
    
    
class Address(models.Model):
    customer = models.OneToOneField("Customer", on_delete=models.CASCADE, primary_key=True)
    province = models.CharField(max_length=100, verbose_name=_('province'))
    city = models.CharField(max_length=100, verbose_name=_('city'))
    street = models.TextField(verbose_name=_('street'))

    
class Order(models.Model):
    ORDER_STATUS_PAID = 'P'
    ORDER_STATUS_UNPAID = 'UN'
    ORDER_STATUS_WAITING = 'W'
    ORDER_STATUS = (
        (ORDER_STATUS_UNPAID, 'Unpaid'),
        (ORDER_STATUS_PAID, 'Paid'),
        (ORDER_STATUS_WAITING, 'Waiting')
    )
    
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, related_name='order')
    datetime_created = models.DateTimeField(default=timezone.now , verbose_name=_('date of created'))
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default=ORDER_STATUS_UNPAID)
    
    
class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='items')
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name=_('quantity'))
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = [['order', 'product']]
        
        
class Cart(models.Model):
    created_at = models.DateTimeField(default=timezone.now, verbose_name=_('created_at'))


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='items')
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name=_('quantity'))
    
    class Meta:
        unique_together = [['cart', 'product']]


class Comment(models.Model):
    COMMENT_STATUS_NOT_APPROVED = 'NA'
    COMMENT_STATUS_APPROVED = 'A'
    COMMENT_STATUS_WAITING = 'W'
    COMMENT_STATUS = (
        (COMMENT_STATUS_NOT_APPROVED, _('Not Approved')),
        (COMMENT_STATUS_APPROVED, _('Approved')),
        (COMMENT_STATUS_WAITING, _('Waiting'))
    )
    text = models.TextField(verbose_name=_('text'))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    status = models.CharField(max_length=20, choices=COMMENT_STATUS, default=COMMENT_STATUS_WAITING)
    datetime_created = models.DateTimeField(default=timezone.now , verbose_name=_('date of created'))


# Generated by Django 5.1.4 on 2024-12-24 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='price',
            new_name='unit_price',
        ),
    ]

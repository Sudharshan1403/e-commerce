# Generated by Django 4.2.2 on 2023-07-28 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nammashop', '0012_rename_user_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.IntegerField(null=True),
        ),
    ]

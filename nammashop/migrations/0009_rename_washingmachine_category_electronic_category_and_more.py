# Generated by Django 4.2.2 on 2023-07-20 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nammashop', '0008_laptop_category_mobile_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WashingMachine_Category',
            new_name='Electronic_Category',
        ),
        migrations.DeleteModel(
            name='Laptop_Category',
        ),
        migrations.DeleteModel(
            name='Mobile_Category',
        ),
    ]

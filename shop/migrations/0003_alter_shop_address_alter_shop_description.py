# Generated by Django 4.1.7 on 2023-04-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shop_address_shop_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]

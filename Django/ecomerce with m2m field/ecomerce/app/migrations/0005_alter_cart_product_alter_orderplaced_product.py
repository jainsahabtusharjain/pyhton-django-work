# Generated by Django 4.1.3 on 2022-12-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_cart_product_alter_orderplaced_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="product",
            field=models.ManyToManyField(to="app.product"),
        ),
        migrations.AlterField(
            model_name="orderplaced",
            name="product",
            field=models.ManyToManyField(to="app.product"),
        ),
    ]

# Generated by Django 3.2.1 on 2024-06-18 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0016_cart_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.1 on 2024-06-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0007_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 3.2.1 on 2024-06-17 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0004_book_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='count',
            new_name='book_count',
        ),
    ]

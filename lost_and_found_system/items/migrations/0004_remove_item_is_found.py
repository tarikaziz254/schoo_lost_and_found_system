# Generated by Django 5.1.3 on 2024-12-01 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_found',
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_remove_item_is_found'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('lost', 'Lost'), ('found', 'Found'), ('picked', 'picked')], default='lost', max_length=10),
        ),
    ]

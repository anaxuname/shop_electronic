# Generated by Django 5.0.4 on 2024-05-10 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date_reliease',
            new_name='date_release',
        ),
    ]

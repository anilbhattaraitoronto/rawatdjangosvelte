# Generated by Django 3.1.2 on 2020-10-04 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201004_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'name']},
        ),
    ]

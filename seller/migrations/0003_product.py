# Generated by Django 5.0.3 on 2024-03-22 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField(max_length=100, null=True)),
                ('description', models.TextField(max_length=100, null=True)),
                ('price', models.TextField(null=True)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.category')),
            ],
        ),
    ]
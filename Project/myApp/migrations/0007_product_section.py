# Generated by Django 5.0.4 on 2024-06-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_delete_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.CharField(blank=True, choices=[('Most Popular Books', 'Most Popular Books'), ('Best Sellers', 'Best Sellers'), ('Weekly Best Seller', 'Weekly Best Seller')], max_length=50, null=True),
        ),
    ]

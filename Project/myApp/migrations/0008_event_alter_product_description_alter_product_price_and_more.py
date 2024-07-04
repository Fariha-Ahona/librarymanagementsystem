# Generated by Django 5.0.4 on 2024-06-23 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_product_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/events/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='section',
            field=models.CharField(choices=[('most_popular', 'Most Popular'), ('best_sellers', 'Best Sellers'), ('weekly_best_sellers', 'Weekly Best Sellers')], default='most_popular', max_length=50),
        ),
    ]
# Generated by Django 4.2.1 on 2023-11-30 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='AvailableProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
            ],
        ),
    ]
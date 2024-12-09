# Generated by Django 5.1.4 on 2024-12-07 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_customer_account_customer_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='email_address',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sales.bill')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Producttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=300)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='sales.Producttype', to='sales.product'),
        ),
    ]
# Generated by Django 5.1.4 on 2024-12-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='newsletter_abo',
            field=models.BooleanField(default=True),
        ),
    ]

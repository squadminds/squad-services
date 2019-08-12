# Generated by Django 2.2.3 on 2019-07-19 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999)]),
        ),
    ]

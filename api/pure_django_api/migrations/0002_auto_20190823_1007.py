# Generated by Django 2.2.4 on 2019-08-23 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pure_django_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ('id',)},
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-06 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210306_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 14, 4, 54, 969288)),
        ),
    ]

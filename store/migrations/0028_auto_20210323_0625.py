# Generated by Django 3.1.7 on 2021-03-23 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_auto_20210315_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 23, 6, 25, 33, 954303)),
        ),
    ]

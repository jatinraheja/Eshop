# Generated by Django 3.1.7 on 2021-03-15 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_auto_20210315_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 15, 5, 6, 22, 196112)),
        ),
    ]

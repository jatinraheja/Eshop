# Generated by Django 3.1.7 on 2021-03-25 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20210323_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 25, 10, 57, 58, 71179)),
        ),
    ]

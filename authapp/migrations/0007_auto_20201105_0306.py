# Generated by Django 3.1.2 on 2020-11-05 03:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20201105_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 3, 6, 11, 798905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='age',
            field=models.PositiveIntegerField(default=18, verbose_name='возраст'),
        ),
    ]

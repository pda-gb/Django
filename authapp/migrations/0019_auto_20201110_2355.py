# Generated by Django 3.1.2 on 2020-11-10 23:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0018_auto_20201110_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 23, 55, 24, 832220, tzinfo=utc)),
        ),
    ]
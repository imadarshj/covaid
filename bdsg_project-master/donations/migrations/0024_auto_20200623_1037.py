# Generated by Django 2.2.8 on 2020-06-23 10:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0023_auto_20200623_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequest',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 10, 37, 25, 253369, tzinfo=utc), max_length=255),
        ),
    ]
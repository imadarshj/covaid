# Generated by Django 3.0.6 on 2020-05-12 19:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200512_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 12, 19, 39, 3, 208180, tzinfo=utc)),
        ),
    ]

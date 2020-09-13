# Generated by Django 2.2.4 on 2020-05-26 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonationCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]

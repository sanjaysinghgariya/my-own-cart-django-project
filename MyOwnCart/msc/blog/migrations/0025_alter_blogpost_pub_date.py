# Generated by Django 4.1.7 on 2023-05-05 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_blogpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2023, 5, 5, 14, 56, 44, 457180)),
        ),
    ]

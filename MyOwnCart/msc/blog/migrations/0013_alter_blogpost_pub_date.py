# Generated by Django 4.1.7 on 2023-05-03 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blogpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2023, 5, 3, 17, 39, 12, 709368)),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-02 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2023, 5, 2, 7, 16, 45, 619468)),
        ),
    ]

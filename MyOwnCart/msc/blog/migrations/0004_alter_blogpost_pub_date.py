# Generated by Django 4.1.7 on 2023-05-02 00:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(blank=True, verbose_name=datetime.datetime(2023, 5, 2, 6, 6, 45, 722170)),
        ),
    ]

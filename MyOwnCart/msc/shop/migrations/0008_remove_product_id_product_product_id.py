# Generated by Django 4.1.7 on 2023-05-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_contact_phone_alter_orders_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.AutoField(default=400, primary_key=True, serialize=False),
        ),
    ]

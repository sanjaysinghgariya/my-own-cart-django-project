# Generated by Django 4.1.7 on 2023-05-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='makeblog',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('heading0', models.CharField(max_length=50)),
                ('cheading0', models.CharField(max_length=500)),
                ('heading1', models.CharField(max_length=50)),
                ('cheading1', models.CharField(max_length=500)),
                ('sub_heading', models.CharField(max_length=50)),
                ('csub_heading', models.CharField(max_length=500)),
            ],
        ),
    ]

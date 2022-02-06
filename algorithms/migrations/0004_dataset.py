# Generated by Django 3.2.11 on 2022-02-02 00:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0003_algorithmtype_algo_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_data', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('bar_width', models.IntegerField()),
                ('max_bar', models.IntegerField()),
            ],
        ),
    ]

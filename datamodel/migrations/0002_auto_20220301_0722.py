# Generated by Django 3.2.9 on 2022-03-01 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='patient',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='date',
            field=models.DateField(auto_created=True, default=datetime.datetime.now),
        ),
    ]

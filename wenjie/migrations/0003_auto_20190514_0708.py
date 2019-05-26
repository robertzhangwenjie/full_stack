# Generated by Django 2.1.3 on 2019-05-13 23:08

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wenjie', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='change_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='person',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=datetime.datetime(1990, 8, 9, 0, 0)),
        ),
    ]

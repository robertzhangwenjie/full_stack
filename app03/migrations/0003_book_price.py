# Generated by Django 2.1.3 on 2019-05-17 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0002_auto_20190517_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.CharField(default=888, max_length=24),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.3 on 2019-05-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 2.1.3 on 2019-05-16 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hobby', models.CharField(max_length=32)),
                ('phone', models.IntegerField()),
                ('addr', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=6, null=True)),
                ('inventory', models.IntegerField(default=9999)),
                ('quantity_sold', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('addr', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='app01.Publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(to='app01.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.AuthorDetail'),
        ),
    ]

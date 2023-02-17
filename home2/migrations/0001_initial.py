# Generated by Django 3.2.8 on 2022-11-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Anonymous User', max_length=10)),
                ('First_name', models.CharField(max_length=150)),
                ('Last_name', models.CharField(max_length=150)),
                ('Email_id', models.EmailField(max_length=254)),
                ('Mobile_number', models.CharField(max_length=10)),
                ('Message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='email_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('time', models.TimeField()),
                ('releasedate', models.DateField()),
                ('about', models.CharField(max_length=5000)),
                ('starcast', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Anonymous User', max_length=10)),
                ('movie', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('seat', models.CharField(default='A1', max_length=2)),
                ('screen', models.IntegerField(default='1')),
                ('price', models.IntegerField(default='0')),
            ],
        ),
    ]
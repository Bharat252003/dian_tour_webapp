# Generated by Django 3.1.7 on 2021-05-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='', max_length=200)),
                ('fromCity', models.CharField(max_length=100)),
                ('toCity', models.CharField(max_length=100)),
                ('depatureDate', models.DateField()),
                ('days', models.IntegerField(default=1)),
                ('noOfRooms', models.IntegerField()),
                ('noOfAdults', models.IntegerField()),
                ('noOfChildren', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phoneNo', models.CharField(max_length=12)),
                ('amountPerPerson', models.IntegerField(default=0)),
                ('totalAmount', models.FloatField(default=0)),
                ('userName', models.CharField(default='', max_length=200)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=50000)),
                ('days', models.IntegerField(default=1)),
                ('desc', models.TextField()),
                ('offer', models.BooleanField(default=False)),
                ('img1', models.ImageField(upload_to='pics')),
                ('img2', models.ImageField(upload_to='pics')),
                ('img3', models.ImageField(upload_to='pics')),
                ('day1', models.CharField(blank=True, max_length=200, null=True)),
                ('day2', models.CharField(blank=True, max_length=200, null=True)),
                ('day3', models.CharField(blank=True, max_length=200, null=True)),
                ('day4', models.CharField(blank=True, max_length=200, null=True)),
                ('day5', models.CharField(blank=True, max_length=200, null=True)),
                ('day6', models.CharField(blank=True, max_length=200, null=True)),
                ('day7', models.CharField(blank=True, max_length=200, null=True)),
                ('day8', models.CharField(blank=True, max_length=200, null=True)),
                ('day9', models.CharField(blank=True, max_length=200, null=True)),
                ('day10', models.CharField(blank=True, max_length=200, null=True)),
                ('day11', models.CharField(blank=True, max_length=200, null=True)),
                ('day12', models.CharField(blank=True, max_length=200, null=True)),
                ('day13', models.CharField(blank=True, max_length=200, null=True)),
                ('day14', models.CharField(blank=True, max_length=200, null=True)),
                ('day15', models.CharField(blank=True, max_length=200, null=True)),
                ('day16', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]

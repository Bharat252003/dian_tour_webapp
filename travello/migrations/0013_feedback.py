# Generated by Django 4.1.5 on 2023-04-24 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0012_rename_customer_name_payment_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]

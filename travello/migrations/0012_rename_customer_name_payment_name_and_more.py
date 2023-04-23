# Generated by Django 4.1.5 on 2023-04-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0011_alter_confirmbooking_cancel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='customer_num',
            new_name='num',
        ),
        migrations.AddField(
            model_name='payment',
            name='razor_pay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='razor_pay_payment_sign',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

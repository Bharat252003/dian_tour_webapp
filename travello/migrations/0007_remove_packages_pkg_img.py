# Generated by Django 4.1.5 on 2023-04-13 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0006_packages_pkg_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='pkg_img',
        ),
    ]

# Generated by Django 2.1 on 2018-08-04 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180803_0737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='monthreport',
        ),
        migrations.RemoveField(
            model_name='users',
            name='monthreport_content',
        ),
        migrations.RemoveField(
            model_name='users',
            name='weekereport',
        ),
        migrations.RemoveField(
            model_name='users',
            name='weekereport_content',
        ),
    ]

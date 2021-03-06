# Generated by Django 2.1 on 2018-08-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=256)),
                ('schoold', models.IntegerField()),
                ('address', models.CharField(max_length=256)),
                ('latitude', models.CharField(max_length=256)),
                ('longitude', models.CharField(max_length=256)),
                ('playcard', models.CharField(max_length=256)),
                ('weekereport', models.CharField(max_length=256)),
                ('weekereport_content', models.CharField(max_length=256)),
                ('monthreport', models.CharField(max_length=256)),
                ('monthreport_content', models.CharField(max_length=256)),
                ('endtime', models.DateTimeField()),
                ('outtime', models.DateTimeField()),
            ],
        ),
    ]

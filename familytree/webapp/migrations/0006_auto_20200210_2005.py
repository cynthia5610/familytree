# Generated by Django 3.0.3 on 2020-02-11 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200210_1954'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('city', 'state')},
        ),
    ]

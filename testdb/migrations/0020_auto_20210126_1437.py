# Generated by Django 3.1 on 2021-01-26 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0019_auto_20210125_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur_test',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 26, 14, 37, 16, 484374)),
        ),
    ]

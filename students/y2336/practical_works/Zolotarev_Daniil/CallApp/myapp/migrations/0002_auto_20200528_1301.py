# Generated by Django 3.0.6 on 2020-05-28 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='callinformation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='cashinformation',
            name='date_addition',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='usercall',
            name='pay_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
# Generated by Django 3.0.3 on 2020-03-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Levashova_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='state_number',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]

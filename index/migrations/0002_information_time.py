# Generated by Django 3.0.4 on 2020-06-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]

# Generated by Django 3.0.4 on 2020-06-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anima', '0003_m_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anima',
            name='l_ing',
            field=models.ImageField(upload_to='static/ANindex'),
        ),
    ]
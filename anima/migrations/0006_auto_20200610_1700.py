# Generated by Django 3.0.4 on 2020-06-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anima', '0005_m_user_anime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='m_user',
            name='anime',
        ),
        migrations.AddField(
            model_name='m_user',
            name='anime',
            field=models.ManyToManyField(to='anima.Anima'),
        ),
    ]
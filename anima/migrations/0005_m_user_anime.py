# Generated by Django 3.0.4 on 2020-06-10 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anima', '0004_auto_20200609_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='m_user',
            name='anime',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='anima.Anima'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-27 23:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appprojet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tacheuser',
            name='durre',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

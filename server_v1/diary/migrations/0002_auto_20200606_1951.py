# Generated by Django 3.0.5 on 2020-06-06 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaldayentry',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sessionentry',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

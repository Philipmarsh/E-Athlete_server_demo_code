# Generated by Django 3.0.5 on 2020-06-06 18:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20200606_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionentry',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
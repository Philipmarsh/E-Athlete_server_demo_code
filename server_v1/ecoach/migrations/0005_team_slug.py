# Generated by Django 3.0.5 on 2020-09-02 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecoach', '0004_auto_20200901_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.5 on 2020-09-04 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecoach', '0011_auto_20200904_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecoach.Team'),
        ),
    ]
# Generated by Django 3.0.5 on 2020-09-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_coach_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='coach_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]

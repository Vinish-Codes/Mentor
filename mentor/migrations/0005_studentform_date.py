# Generated by Django 5.1.1 on 2024-10-01 15:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0004_studentform_counseling_dates'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentform',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 5.1.1 on 2024-10-03 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0011_studentform_challenges_studentform_opportunities_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentform',
            name='Challenges',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='Opportunities',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='Strengths',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='Weakness',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='ao',
        ),
        migrations.RemoveField(
            model_name='studentform',
            name='nao',
        ),
    ]

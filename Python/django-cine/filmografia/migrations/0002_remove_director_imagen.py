# Generated by Django 4.0.5 on 2022-06-25 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmografia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='imagen',
        ),
    ]

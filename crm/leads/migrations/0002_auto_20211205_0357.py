# Generated by Django 3.1.4 on 2021-12-05 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account_Executive',
            new_name='Account_exec',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='account_executive',
            new_name='account_exec',
        ),
    ]

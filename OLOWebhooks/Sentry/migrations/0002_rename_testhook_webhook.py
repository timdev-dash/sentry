# Generated by Django 4.1.4 on 2022-12-27 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sentry', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestHook',
            new_name='WebHook',
        ),
    ]

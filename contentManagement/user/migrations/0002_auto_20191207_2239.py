# Generated by Django 2.2.7 on 2019-12-07 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='person',
            new_name='User',
        ),
    ]

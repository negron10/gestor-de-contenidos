# Generated by Django 2.2.7 on 2019-12-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20191218_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='createDates',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='createDates',
            field=models.DateField(auto_now_add=True),
        ),
    ]

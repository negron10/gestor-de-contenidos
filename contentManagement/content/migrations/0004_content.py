# Generated by Django 2.2.7 on 2019-12-08 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20191208_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('subtitle', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=1000)),
                ('createDate', models.DateField()),
                ('status', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Category')),
            ],
        ),
    ]
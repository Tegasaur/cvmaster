# Generated by Django 3.0.5 on 2020-05-29 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0016_auto_20200527_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfomodel',
            name='fun_image',
        ),
    ]
# Generated by Django 3.0.5 on 2020-05-16 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20200201_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencemodel',
            name='Information',
            field=models.TextField(verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='involvementmodel',
            name='Information',
            field=models.TextField(verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='skillmodel',
            name='Information',
            field=models.TextField(verbose_name='Details'),
        ),
    ]
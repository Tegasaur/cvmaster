# Generated by Django 3.0.5 on 2020-05-27 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_auto_20200525_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatemodel',
            name='Temp',
            field=models.CharField(choices=[('lumia', 'Lumia'), ('office', 'Office'), ('personal', 'Personal'), ('iportfolio', 'IPortfolio'), ('dewi', 'Dewi')], default='', max_length=30, verbose_name='Pick Your Template'),
        ),
    ]
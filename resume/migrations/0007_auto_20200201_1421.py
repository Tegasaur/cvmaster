# Generated by Django 3.0.2 on 2020-02-01 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_auto_20200131_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinfomodel',
            old_name='image',
            new_name='profile_image',
        ),
        migrations.AddField(
            model_name='personalinfomodel',
            name='balanced_image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='personalinfomodel',
            name='fun_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_remove_home_logo_home_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='title',
            new_name='title1',
        ),
        migrations.AddField(
            model_name='home',
            name='title2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='title3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0005_portfolio_description_portfolio_publish_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='client',
            field=models.CharField(default='', max_length=35),
            preserve_default=False,
        ),
    ]

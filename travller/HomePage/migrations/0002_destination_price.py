# Generated by Django 3.0.4 on 2020-04-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

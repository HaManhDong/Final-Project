# Generated by Django 2.0.3 on 2018-05-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_added_to_blockchain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_enough_images',
            field=models.BooleanField(default=False),
        ),
    ]
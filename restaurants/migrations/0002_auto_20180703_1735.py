# Generated by Django 2.0.4 on 2018-07-03 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='opining_time',
            new_name='opening_time',
        ),
    ]

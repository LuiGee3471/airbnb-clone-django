# Generated by Django 2.2.5 on 2019-12-15 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20191214_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='bath',
            new_name='baths',
        ),
    ]

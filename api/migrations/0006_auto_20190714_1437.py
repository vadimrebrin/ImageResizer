# Generated by Django 2.2.3 on 2019-07-14 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190714_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='original_image',
        ),
        migrations.RemoveField(
            model_name='task',
            name='sized_image',
        ),
    ]
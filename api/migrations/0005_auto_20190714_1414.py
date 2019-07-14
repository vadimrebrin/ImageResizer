# Generated by Django 2.2.3 on 2019-07-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190712_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='extension',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='task',
            name='original_image',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='task',
            name='sized_image',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
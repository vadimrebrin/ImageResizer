# Generated by Django 2.2.3 on 2019-07-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=150, unique=True)),
                ('original_image', models.BinaryField()),
                ('sized_image', models.BinaryField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

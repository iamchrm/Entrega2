# Generated by Django 3.1.3 on 2020-12-07 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created'], 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]

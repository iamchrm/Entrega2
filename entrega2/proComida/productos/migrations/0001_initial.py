# Generated by Django 3.1.3 on 2020-12-07 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='productos', verbose_name='Imagen')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Más información')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'ordering': ['created'],
            },
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-13 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Articulos',
            },
        ),
    ]

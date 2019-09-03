# Generated by Django 2.2.5 on 2019-09-03 00:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('cedula', models.CharField(max_length=11)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]

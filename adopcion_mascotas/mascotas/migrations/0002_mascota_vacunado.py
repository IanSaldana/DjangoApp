# Generated by Django 5.0.4 on 2024-08-18 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='vacunado',
            field=models.BooleanField(default=False),
        ),
    ]

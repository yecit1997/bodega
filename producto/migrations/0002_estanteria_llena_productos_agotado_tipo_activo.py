# Generated by Django 5.0.6 on 2024-07-18 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estanteria',
            name='llena',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productos',
            name='agotado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tipo',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]

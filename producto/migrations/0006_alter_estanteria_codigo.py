# Generated by Django 5.0.6 on 2024-08-25 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_alter_tipo_limite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estanteria',
            name='codigo',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'), ('A6', 'A6'), ('A7', 'A7')], max_length=20, unique=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-08-09 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_estanteria_llena_productos_agotado_tipo_activo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estanteria',
            options={'ordering': ['codigo'], 'verbose_name': 'Estanteria', 'verbose_name_plural': 'Estanterias'},
        ),
        migrations.AlterModelOptions(
            name='tipo',
            options={'ordering': ['tipo'], 'verbose_name': 'Tipo', 'verbose_name_plural': 'Tipos'},
        ),
        migrations.AlterField(
            model_name='tipo',
            name='tipo',
            field=models.CharField(choices=[('Llantas y Rines', 'Llantas y Rines'), ('Guayas y Kit de arrastre', 'Guayas y Kit de arrastre'), ('Luces y Estacionarias', 'Luces y Estacionarias'), ('Bocinas', 'Bocinas'), ('Motores', 'Motores'), ('Cojines', 'Cojines'), ('Espejos', 'Espejos')], max_length=100, unique=True),
        ),
    ]

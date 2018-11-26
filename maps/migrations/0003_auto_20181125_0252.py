# Generated by Django 2.1.3 on 2018-11-25 02:52

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_mapas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mapas',
            options={'verbose_name': 'Map', 'verbose_name_plural': 'Maps'},
        ),
        migrations.AlterField(
            model_name='mapas',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]

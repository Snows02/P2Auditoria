# Generated by Django 2.0.7 on 2018-11-20 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numerals', '0004_subnumeral'),
    ]

    operations = [
        migrations.AddField(
            model_name='subnumeral',
            name='info',
            field=models.CharField(default='No hay documentos obligatorios, sin embargo se aconseja constatar todo control a través de un documento, físico o digital.', max_length=1024),
        ),
    ]

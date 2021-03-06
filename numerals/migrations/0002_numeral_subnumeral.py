# Generated by Django 2.0.7 on 2018-11-20 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('numerals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numeral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position_in_menu', models.PositiveIntegerField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='numerals.Title')),
            ],
            options={
                'verbose_name': 'Numeral',
                'verbose_name_plural': 'Numerales',
                'ordering': ['position_in_menu'],
            },
        ),
        migrations.CreateModel(
            name='SubNumeral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position_in_menu', models.PositiveIntegerField()),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='numerals.Title')),
            ],
            options={
                'verbose_name': 'SubNumeral',
                'verbose_name_plural': 'SubNumerales',
                'ordering': ['position_in_menu'],
            },
        ),
    ]

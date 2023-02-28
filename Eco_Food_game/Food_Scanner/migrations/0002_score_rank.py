# Generated by Django 4.1.7 on 2023-02-24 11:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Scanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=16, unique=True, verbose_name='Player Number')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(1)], verbose_name='Score')),
            ],
            options={
                'verbose_name': 'Score List',
                'verbose_name_plural': 'Score List',
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('c_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Food_Scanner.score')),
                ('rank', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Rank')),
            ],
        ),
    ]

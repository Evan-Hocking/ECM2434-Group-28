# Generated by Django 4.1.7 on 2023-02-24 12:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Scanner', '0003_alter_demo_options_alter_demo_userscore_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='rank',
            field=models.IntegerField(default=9999, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Rank'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Rank',
        ),
    ]
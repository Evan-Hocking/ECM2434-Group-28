# Generated by Django 4.1.5 on 2023-02-27 16:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Scanner', '0005_alter_demo_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='client',
        ),
        migrations.AddField(
            model_name='score',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Food_Scanner.demo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='score',
            name='rank',
            field=models.IntegerField(default=9999, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Rank'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='userScore',
            field=models.IntegerField(default=0, verbose_name='Score'),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(0)], verbose_name='Score'),
        ),
    ]
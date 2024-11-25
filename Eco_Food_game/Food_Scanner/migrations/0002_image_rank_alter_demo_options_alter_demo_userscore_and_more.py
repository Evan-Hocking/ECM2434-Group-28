# Generated by Django 4.1.5 on 2023-03-22 23:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Scanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='image', max_length=200)),
                ('image', models.ImageField(upload_to='barcode_imgs')),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('c_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Food_Scanner.demo')),
                ('rank', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='rank')),
            ],
        ),
        migrations.AlterModelOptions(
            name='demo',
            options={'verbose_name': 'Player List', 'verbose_name_plural': 'Player List'},
        ),
        migrations.AlterField(
            model_name='demo',
            name='userScore',
            field=models.IntegerField(default=0, verbose_name='Score'),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(0)], verbose_name='Score')),
                ('rank', models.IntegerField(default=9999, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Rank')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food_Scanner.demo')),
            ],
            options={
                'verbose_name': 'Score List',
                'verbose_name_plural': 'Score List',
            },
        ),
    ]

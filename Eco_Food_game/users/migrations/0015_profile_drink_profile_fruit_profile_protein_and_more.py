# Generated by Django 4.1.5 on 2023-03-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_merge_20230302_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Drink',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Fruit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Protein',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Snack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='Vegetable',
            field=models.IntegerField(default=0),
        ),
    ]
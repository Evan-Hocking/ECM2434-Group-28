# Generated by Django 4.1.5 on 2023-03-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_merge_20230302_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.1.5 on 2023-03-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='image',
            field=models.CharField(blank=True, max_length=9999),
        ),
    ]

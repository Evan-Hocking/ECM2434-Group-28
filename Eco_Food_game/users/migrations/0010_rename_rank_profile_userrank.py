# Generated by Django 4.1.5 on 2023-03-02 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='rank',
            new_name='userRank',
        ),
    ]

# Generated by Django 4.1.5 on 2023-03-22 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food_Scanner', '0010_image_name_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='barcode_imgs'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_home_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(default='', upload_to='Home/images'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.ImageField(default='', upload_to='photo/images'),
        ),
    ]

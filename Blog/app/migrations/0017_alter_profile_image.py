# Generated by Django 4.0.3 on 2023-04-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_profile_country_remove_profile_mobileno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images'),
        ),
    ]

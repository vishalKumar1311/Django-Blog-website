# Generated by Django 4.0.3 on 2023-04-11 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, choices=[('Development', 'Development'), ('Food', 'Food'), ('Travel', 'Travel'), ('Lifestyle', 'Lifestyle'), ('Fashion', 'Fashion'), ('Personal', 'Personal')], max_length=50),
        ),
    ]

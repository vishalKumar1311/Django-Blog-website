# Generated by Django 4.0.3 on 2023-02-08 16:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_comment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
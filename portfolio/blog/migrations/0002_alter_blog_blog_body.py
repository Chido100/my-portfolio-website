# Generated by Django 4.2.16 on 2024-09-04 09:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_body',
            field=ckeditor.fields.RichTextField(verbose_name='Blog Body'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_skills_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill_image',
            field=models.ImageField(upload_to='skill_images'),
        ),
    ]

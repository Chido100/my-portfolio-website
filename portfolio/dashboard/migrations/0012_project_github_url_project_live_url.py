# Generated by Django 4.2.16 on 2024-09-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_remove_project_tech_stack_project_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='live_url',
            field=models.URLField(default=''),
        ),
    ]
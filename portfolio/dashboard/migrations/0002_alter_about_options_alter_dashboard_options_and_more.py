# Generated by Django 5.0.1 on 2024-01-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='dashboard',
            options={'verbose_name_plural': 'Dashboard'},
        ),
        migrations.AddField(
            model_name='dashboard',
            name='intro',
            field=models.TextField(default='Hi there...'),
        ),
    ]

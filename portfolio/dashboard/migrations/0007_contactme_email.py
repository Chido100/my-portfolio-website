# Generated by Django 5.0.1 on 2024-08-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0006_alter_skills_skill_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactme",
            name="email",
            field=models.EmailField(default="youremail@email.com", max_length=254),
        ),
    ]
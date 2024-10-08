# Generated by Django 5.0.1 on 2024-08-18 15:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="blog_image")),
                ("blog_intro", models.TextField(verbose_name="Blog Introduction")),
                ("blog_body", models.TextField(verbose_name="Blog Body")),
                ("blog_closure", models.TextField(verbose_name="Blog Closure")),
                ("date_created", models.DateField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="poster",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-date_created",),
            },
        ),
    ]

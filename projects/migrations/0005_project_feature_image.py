# Generated by Django 4.1.6 on 2023-03-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0004_tag_project_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="feature_image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]

# Generated by Django 5.0 on 2023-12-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_meta_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="meta_text",
            field=models.CharField(
                default="This blog gives valuable insights", max_length=255
            ),
        ),
    ]

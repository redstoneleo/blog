# Generated by Django 4.1.3 on 2023-11-10 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_alter_post_options_alter_post_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="firstReleaseDate",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.1.3 on 2023-11-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0014_alter_post_firstreleasedate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="firstReleaseDate",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="latestRevisionDate",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.1.3 on 2023-11-09 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_post_firstreleasedate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="firstReleaseDate",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="latestrevisionDate",
            field=models.DateField(auto_now=True),
        ),
    ]

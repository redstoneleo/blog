# Generated by Django 4.1.3 on 2023-11-09 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_alter_post_firstreleasedate_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["latestRevisionDate"]},
        ),
        migrations.RenameField(
            model_name="post",
            old_name="latestrevisionDate",
            new_name="latestRevisionDate",
        ),
    ]

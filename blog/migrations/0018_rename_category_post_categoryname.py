# Generated by Django 4.1.3 on 2023-11-11 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0017_alter_post_firstreleasedate_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="category",
            new_name="categoryName",
        ),
    ]
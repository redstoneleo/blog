# Generated by Django 4.1.3 on 2023-11-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.CharField(
                choices=[
                    ("高等数学", "Math"),
                    ("我的软件", "Mysoftware"),
                    ("付费服务", "Paidservice"),
                ],
                max_length=4,
            ),
        ),
    ]

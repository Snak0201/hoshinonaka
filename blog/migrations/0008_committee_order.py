# Generated by Django 4.1.1 on 2022-09-10 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_article_committees_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="committee",
            name="order",
            field=models.PositiveSmallIntegerField(default=0, verbose_name="配置順"),
        ),
    ]
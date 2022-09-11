# Generated by Django 4.1.1 on 2022-09-11 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_article_bureau_article_committees_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bureau",
            name="name_en",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="局英語名"
            ),
        ),
        migrations.AddField(
            model_name="committee",
            name="name_en",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="委員会英語名"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="bureau",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="article_bureau",
                to="blog.bureau",
                verbose_name="局",
            ),
        ),
    ]

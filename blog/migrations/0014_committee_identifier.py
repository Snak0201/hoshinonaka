# Generated by Django 4.1.1 on 2022-09-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_bureau_name_en_committee_name_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="committee",
            name="identifier",
            field=models.SlugField(blank=True, null=True, verbose_name="委員会識別子"),
        ),
    ]

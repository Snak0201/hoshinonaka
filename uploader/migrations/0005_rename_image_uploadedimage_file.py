# Generated by Django 4.1.1 on 2022-09-10 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("uploader", "0004_uploadedfile_name_uploadedimage_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="uploadedimage",
            old_name="image",
            new_name="file",
        ),
    ]

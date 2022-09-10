from django.db import models
import os
import datetime

# Create your models here.
def generate_media_path(instance, file_name):
    if instance.name:
        file_name = instance.name + os.path.splitext(file_name)[1]
    date = datetime.datetime.now().strftime("%Y/%m/%d")
    path = os.path.join(os.path.splitext(file_name)[1], date, file_name)
    return path


class UploadedImage(models.Model):
    file = models.ImageField(verbose_name="画像", upload_to=generate_media_path)
    name = models.CharField(verbose_name="ファイル名", max_length=128, blank=True, null=True)

    def __str__(self):
        return self.file.url


class UploadedFile(models.Model):
    file = models.FileField(verbose_name="ファイル", upload_to=generate_media_path)
    name = models.CharField(verbose_name="ファイル名", max_length=128, blank=True, null=True)

    def __str__(self):
        return self.file.url

from django.db import models
import os
import datetime

# Create your models here.
def generate_media_path(instance, file_name):
    date = datetime.datetime.now().strftime("%Y/%m/%d")
    path = os.path.join(os.path.splitext(file_name)[1], date, file_name)
    return path


class UploadedImage(models.Model):
    image = models.ImageField(verbose_name="画像", upload_to=generate_media_path)

    def __str__(self):
        return self.image.url

class UploadedFile(models.Model):
    file = models.FileField(verbose_name="ファイル", upload_to=generate_media_path)

    def __str__(self):
        return self.file.url
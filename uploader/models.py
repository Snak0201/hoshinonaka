from django.db import models

# Create your models here.
class UploadedImage(models.Model):
    image = models.ImageField(verbose_name="画像")

    def __str__(self):
        return self.image.url

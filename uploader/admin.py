from django.contrib import admin
from .models import UploadedImage, UploadedFile

# Register your models here.
admin.site.register((UploadedImage, UploadedFile))

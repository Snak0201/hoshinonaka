from dataclasses import fields
from django.forms import ModelForm
from .models import UploadedImage, UploadedFile


class UploadImageForm(ModelForm):
    class Meta:
        model = UploadedImage
        fields = "__all__"


class UploadFileForm(ModelForm):
    class Meta:
        model = UploadedFile
        fields = "__all__"
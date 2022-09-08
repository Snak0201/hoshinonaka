from dataclasses import fields
from django.forms import ModelForm
from .models import UploadedImage


class UploadImageForm(ModelForm):
    class Meta:
        model = UploadedImage
        fields = "__all__"

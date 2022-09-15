from rest_framework.serializers import ModelSerializer
from blog.models import Bureau
from uploader.models import UploadedImage


class BureauSerializer(ModelSerializer):
    class Meta:
        model = Bureau
        fields = "__all__"


class UploadedImageSerializer(ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = "__all__"


class ImageUploadSerializer(ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ("file", "name")

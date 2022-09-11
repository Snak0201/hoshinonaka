from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import (
    BureauSerializer,
    UploadedImageSerializer,
    ImageUploadSerializer,
)
from blog.models import Bureau
from uploader.models import UploadedImage

# Create your views here.
class BureauListView(ListAPIView):
    serializer_class = BureauSerializer
    queryset = Bureau.objects.all()


class BureauView(RetrieveAPIView):
    serializer_class = BureauSerializer
    queryset = Bureau.objects.all()
    lookup_field = "code"


class UploadedImageListView(ListAPIView):
    serializer_class = UploadedImageSerializer
    queryset = UploadedImage.objects.all()


class UploadedImageView(RetrieveAPIView):
    serializer_class = UploadedImageSerializer
    queryset = UploadedImage.objects.all()


class ImageUploadView(CreateAPIView):
    serializer_class = ImageUploadSerializer

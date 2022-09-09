from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import UploadImageForm
from .models import UploadedImage

# Create your views here.
class UploadImageView(CreateView):
    model = UploadedImage
    form_class = UploadImageForm
    template_name = "uploader/image.html"
    success_url = reverse_lazy("uploader:images")


class UploadedMediaListView(ListView):
    model = UploadedImage
    template_name = "uploader/file_list.html"


image = UploadImageView.as_view()
media = UploadedMediaListView.as_view()

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import UploadImageForm, UploadFileForm
from .models import UploadedFile, UploadedImage

# Create your views here.
class UploadImageView(CreateView):
    model = UploadedImage
    form_class = UploadImageForm
    template_name = "uploader/image.html"
    success_url = reverse_lazy("uploader:media")


class UploadFileView(CreateView):
    model = UploadedFile
    form_class = UploadFileForm
    template_name = "uploader/file.html"
    success_url = reverse_lazy("uploader:media")


class UploadedMediaListView(ListView):
    model = UploadedImage
    template_name = "uploader/media.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["file_list"] = UploadedFile.objects.all()
        return context


image = UploadImageView.as_view()
file = UploadFileView.as_view()
media = UploadedMediaListView.as_view()

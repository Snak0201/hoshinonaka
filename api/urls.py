from . import apis
from django.urls import path

urlpatterns = [
    path("bureaus/", apis.BureauListView.as_view()),
    path("bureaus/<slug:code>/", apis.BureauView.as_view()),
    path("uploaders/", apis.UploadedImageListView.as_view()),
    path("uploaders/<int:pk>/", apis.UploadedImageView.as_view()),
    path("uploaders/upload/", apis.ImageUploadView.as_view()),
]

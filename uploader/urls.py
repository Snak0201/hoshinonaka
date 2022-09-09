from django.urls import path
from . import views

app_name = "uploader"

urlpatterns = [
    path("", views.file_list, name="file_list"),
    path("image/", views.image, name="image"),
]

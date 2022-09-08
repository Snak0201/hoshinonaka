from django.urls import path
from . import views

app_name = "uploader"

urlpatterns = [
    path("", views.images, name="images"),
    path("image/", views.image, name="image"),
]

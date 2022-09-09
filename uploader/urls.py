from django.urls import path
from . import views

app_name = "uploader"

urlpatterns = [
    path("", views.media, name="media"),
    path("image/", views.image, name="image"),
]

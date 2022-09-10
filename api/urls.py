from . import apis
from django.urls import path

urlpatterns = [
    path("bureaus/", apis.BureauList.as_view(), name="bureaus"),
]

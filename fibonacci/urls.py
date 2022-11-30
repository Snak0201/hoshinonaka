from django.urls import path

from . import apis

app_name = "fibonacci"

urlpatterns = [path("fib", apis.FibonacciAPIView.as_view())]

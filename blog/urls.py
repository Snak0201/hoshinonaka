from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("articles/", views.ArticleListView.as_view(), name="articles"),
    path("articles/<int:article_id>/", views.ArticleView.as_view(), name="article"),
    path("bureaus/<slug:code>/", views.BureauView.as_view(), name="bureau"),
    path("committees/", views.CommitteeListView.as_view(), name="committees"),
    path(
        "committees/<slug:code>/",
        views.CommitteeView.as_view(),
        name="committee",
    ),
]

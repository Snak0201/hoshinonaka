from django.views.generic import TemplateView, DetailView, ListView
from .models import Article, Bureau

# Create your views here.
class IndexView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bureaus"] = Bureau.objects.all().order_by("order")
        return context


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/articles.html"


class ArticleView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog/article.html"
    pk_url_kwarg = "article_id"


class BureauView(DetailView):
    model = Bureau
    context_object_name = "bureau"
    template_name = "blog/bureau.html"
    pk_url_kwarg = "bureau_code"

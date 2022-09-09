from django.views.generic import TemplateView, DetailView, ListView
from .models import Article

# Create your views here.
class IndexView(TemplateView):
    template_name = "blog/index.html"


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/articles.html"


class ArticleView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog/article.html"
    pk_url_kwarg = "article_id"

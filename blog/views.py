from django.views.generic import TemplateView, DetailView
from .models import Article

# Create your views here.
class IndexView(TemplateView):
    template_name = "blog/index.html"


class ArticleView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog/article.html"

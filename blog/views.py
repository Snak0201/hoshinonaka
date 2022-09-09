from django.views.generic import TemplateView, DetailView

# Create your views here.
class IndexView(TemplateView):
    template_name = "blog/index.html"


class ArticleView(DetailView):
    pass

from multiprocessing import context
from django.views.generic import TemplateView, DetailView, ListView
from .models import Article, Bureau, Committee

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = self.kwargs.get(self.pk_url_kwarg)
        context["articles"] = Article.objects.filter(bureau=code).order_by("updated_at")
        context["committees"] = Committee.objects.filter(related_bureaus=code).order_by(
            "order"
        )
        return context


class CommitteeView(DetailView):
    model = Committee
    context_object_name = "committee"
    template_name = "blog/committee.html"
    pk_url_kwarg = "committee_code"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = self.kwargs.get(self.pk_url_kwarg)
        context["articles"] = Article.objects.filter(committees=code).order_by(
            "updated_at"
        )
        return context

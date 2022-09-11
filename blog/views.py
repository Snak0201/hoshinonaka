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
    queryset = Article.objects.filter(is_draft=False).order_by("updated_at")


class ArticleView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog/article.html"
    pk_url_kwarg = "article_id"

    def get_object(self):
        article = super().get_object(
            Article.objects.filter(
                id=self.kwargs.get(self.pk_url_kwarg), is_draft=False
            )
        )
        return article


class BureauView(DetailView):
    model = Bureau
    context_object_name = "bureau"
    template_name = "blog/bureau.html"

    def get_object(self):
        return Bureau.objects.get(code=self.kwargs["code"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bureau = Bureau.objects.get(code=self.kwargs["code"]).id
        context["articles"] = Article.objects.filter(
            bureau=bureau, is_draft=False
        ).order_by("updated_at")
        context["committees"] = Committee.objects.filter(
            related_bureaus=bureau
        ).order_by("order")
        return context


class CommitteeListView(ListView):
    model = Committee
    context_object_name = "committees"
    template_name = "blog/committees.html"


class CommitteeView(DetailView):
    model = Committee
    context_object_name = "committee"
    template_name = "blog/committee.html"

    def get_object(self):
        return Committee.objects.get(code=self.kwargs["code"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        committee = Committee.objects.get(code=self.kwargs["code"]).id
        context["articles"] = Article.objects.filter(
            committees=committee, is_draft=False
        ).order_by("updated_at")
        return context

from django.db import models
from markdown import Markdown

# Create your models here.

CONFIGS = {"codehilite": {"noclasses": True}}
EXTENSIONS = ["extra", "fenced_code", "sane_lists"]


class Bureau(models.Model):
    code = models.SlugField(verbose_name="局コード", unique=True, max_length=4)
    name = models.CharField(verbose_name="局名", max_length=8)
    name_en = models.CharField(
        verbose_name="局英語名", max_length=128, blank=True, null=True
    )
    order = models.PositiveSmallIntegerField(verbose_name="配置順", default=0)
    markdown_text = models.TextField(verbose_name="局紹介（マークダウン）", blank=True, null=True)

    def text(self):
        markdown = Markdown(extensions=EXTENSIONS, extension_configs=CONFIGS)
        return markdown.convert(self.markdown_text)

    def __str__(self):
        return self.name


class Committee(models.Model):
    code = models.SlugField(verbose_name="委員会コード", unique=True, max_length=16)
    identifier = models.SlugField(verbose_name="委員会識別子", unique=True)
    name = models.CharField(verbose_name="委員会名", max_length=32)
    name_en = models.CharField(
        verbose_name="委員会英語名", max_length=128, blank=True, null=True
    )
    order = models.PositiveSmallIntegerField(verbose_name="配置順", default=0)
    markdown_text = models.TextField(
        verbose_name="委員会紹介（マークダウン）", blank=True, null=True
    )
    related_bureaus = models.ManyToManyField(
        Bureau,
        related_name="division_bureaus",
        verbose_name="関連局",
        blank=True,
    )

    def text(self):
        markdown = Markdown(extensions=EXTENSIONS, extension_configs=CONFIGS)
        return markdown.convert(self.markdown_text)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=128)
    markdown_text = models.TextField(verbose_name="本文（マークダウン）")
    bureau = models.ForeignKey(
        Bureau,
        on_delete=models.SET_NULL,
        related_name="article_bureau",
        verbose_name="局",
        blank=True,
        null=True,
    )
    committees = models.ManyToManyField(
        Committee,
        related_name="article_divisions",
        verbose_name="委員会",
        blank=True,
    )
    is_draft = models.BooleanField(verbose_name="下書き", default=False)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="最終更新日時", auto_now=True)

    def text(self):
        markdown = Markdown(extensions=EXTENSIONS, extension_configs=CONFIGS)
        return markdown.convert(self.markdown_text)

    def __str__(self):
        return self.title

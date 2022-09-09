from distutils import extension
from django.db import models
from markdown import Markdown

# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=128)
    markdown_text = models.TextField(verbose_name="本文（マークダウン記述）")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="最終更新日時", auto_now=True)

    def text(self):
        configs = {"codehilite": {"noclasses": True}}

        markdown = Markdown(
            extensions=["extra", "fenced_code", "sane_lists"], extension_configs=configs
        )
        return markdown.convert(self.markdown_text)

    def __str__(self):
        return self.title

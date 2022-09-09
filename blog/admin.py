from django.contrib import admin
from .models import Article, Bureau

# Register your models here.
admin.site.register((Article, Bureau))

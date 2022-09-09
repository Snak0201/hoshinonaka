from django.contrib import admin
from .models import Article, Bureau, Committee

# Register your models here.
admin.site.register((Article, Bureau, Committee))

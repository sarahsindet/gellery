from django.contrib import admin
from .models import Image, Category, Location

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('Category')

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)

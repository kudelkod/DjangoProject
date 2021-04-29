from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Example)
admin.site.register(models.Book)
admin.site.register(models.Publication)
admin.site.register(models.Article)


class AuthorAdmin(admin.ModelAdmin):
    # list_display = ['name', 'surname']
    # exclude = ['name']
    # fields = ['surname']
    list_display = [field.name for field in models.Author._meta.fields]
    list_filter = ['name']
    # search_fields = ['name']
    search_fields = [field.name for field in models.Author._meta.fields]

    class Meta:
        model = models.Author


admin.site.register(models.Author, AuthorAdmin)

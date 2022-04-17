from django.contrib import admin
from .models import Bb, Rubric


# Register your models here.


@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    list_display_links = ('title', 'content')
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    search_fields = ('title', 'content',)


admin.site.register(Rubric)

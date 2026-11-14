from django.contrib import admin

from .models import Category, Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "category", "created_at")
    list_filter = ("status", "category", "tags")
    search_fields = ("title", "description")
    filter_horizontal = ("tags",)


admin.site.register(Category)
admin.site.register(Tag)
from django.urls import path
from .views import (
    TaskListCreateView,
    TaskDetailView,
    CategoryListCreateView,
    TagListCreateView
)

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),

    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("tags/", TagListCreateView.as_view(), name="tag-list"),
]
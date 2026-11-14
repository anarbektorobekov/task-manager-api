from rest_framework import generics

from .models import Task, Category, Tag
from .serializers import (
    TaskListSerializer,
    TaskDetailSerializer,
    CategorySerializer,
    TagSerializer,
)


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = (
        Task.objects.select_related("category")
        .prefetch_related("tags")
        .order_by("-created_at")
    )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TaskDetailSerializer
        return TaskListSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.select_related("category").prefetch_related("tags")
    serializer_class = TaskDetailSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
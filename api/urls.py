from django.urls import path
from .views import CategoryListView, CategoryDetailView, TaskListView, TaskDetailView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories-list-create'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('tasks/', TaskListView.as_view(), name='tasks-list-create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]

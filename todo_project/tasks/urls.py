from django.urls import path
from .views import (
    task_list, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    UserLoginView, UserLogoutView, UserRegistrationView, HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', task_list, name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]

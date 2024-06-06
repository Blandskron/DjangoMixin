from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm, TaskForm
from .models import Task



class HomeView(TemplateView):
    template_name = 'tasks/home.html'

class UserLoginView(LoginView):
    template_name = 'tasks/login.html'

class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return redirect(self.success_url)


@login_required
def task_list(request):
    tasks = Task.objects.filter(created_by=request.user)
    username = request.user.username
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'username': username})

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

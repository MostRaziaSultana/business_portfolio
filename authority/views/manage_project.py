from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404, redirect
from django.forms import inlineformset_factory

from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Import Models
from home.models import (
   Project
)
from authority.forms import ProjectForm

# <<----------------- List, Add, Update, Delete Projects ---------------->>

class ProjectListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Project List'
        return context


class AddProjectView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Project
    fields = ['title', 'subtitle', 'category', 'content', 'image']
    template_name = 'project/add_update_project.html'
    success_url = reverse_lazy('authority:project_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Project"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Project Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class UpdateProjectView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'subtitle', 'category', 'content', 'image']
    template_name = 'project/add_update_project.html'
    success_url = reverse_lazy('authority:project_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Project"
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class ProjectDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        messages.success(request, "Project deleted successfully.")
        return redirect('authority:project_list')

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
   Project,Category
)
from authority.forms import ProjectForm,CategoryForm

# <<----------------- List, Add, Update, Delete Projects ---------------->>

class ProjectListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10

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

    def form_valid(self, form):
        messages.success(self.request, "Project Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class ProjectDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        messages.success(request, "Project deleted successfully.")
        return redirect('authority:project_list')


# <<----------------- List, Add, Update, Delete Category ---------------->>


class CategoryListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Category
    template_name = 'project/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category List'
        return context

class AddCategoryView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'project/add_update_category.html'
    success_url = reverse_lazy('authority:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Category"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Category Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)

class UpdateCategoryView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'project/add_update_category.html'
    success_url = reverse_lazy('authority:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Category"
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class CategoryDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        messages.success(request, "Category deleted successfully.")
        return redirect('authority:category_list')
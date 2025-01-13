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
   Logo
)
from authority.forms import LogoForm

# <<----------------- List, Add, Update, Delete Logo ---------------->>


class LogoListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Logo
    template_name = 'logo/logo_list.html'
    context_object_name = 'logos'

    def get_queryset(self):
        return Logo.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Logo List'
        return context


class AddLogoView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Logo
    form_class = LogoForm
    template_name = 'logo/add_update_logo.html'
    success_url = reverse_lazy('authority:logo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Logo"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Logo Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class UpdateLogoView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Logo
    form_class = LogoForm
    template_name = 'logo/add_update_logo.html'
    success_url = reverse_lazy('authority:logo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Logo"
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class LogoDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):

    def post(self, request, pk):
        logo = get_object_or_404(Logo, pk=pk)
        logo.delete()
        messages.success(request, "Logo deleted successfully.")
        return redirect('authority:logo_list')

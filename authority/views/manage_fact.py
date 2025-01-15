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
   Fact
)
from authority.forms import FactForm

# <<----------------- List, Add, Update, Delete Projects ---------------->>


class FactListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Fact
    template_name = 'fact/fact_list.html'
    context_object_name = 'facts'

    def get_queryset(self):
        return Fact.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Feature List'
        return context


class AddFactView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Fact
    form_class = FactForm
    template_name = 'fact/add_update_fact.html'
    success_url = reverse_lazy('authority:fact_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Feature"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Fact Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class UpdateFactView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Fact
    form_class = FactForm
    template_name = 'fact/add_update_fact.html'
    success_url = reverse_lazy('authority:fact_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Feature"
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class FactDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):

    def post(self, request, pk):
        fact = get_object_or_404(Fact, pk=pk)
        fact.delete()
        messages.success(request, "Fact deleted successfully.")
        return redirect('authority:fact_list')

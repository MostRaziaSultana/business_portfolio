from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Import Models
from home.models import Service

from authority.forms import ServiceForm

# <<----------------- List, Add, Update, Delete Service ---------------->>


class ServiceListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Service
    template_name = 'service/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Service List'
        return context


class UpdateServiceView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service/add_update_service.html'
    success_url = reverse_lazy('authority:service_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Service"
        context["updated"] = True
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class AddServiceView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service/add_update_service.html'
    success_url = reverse_lazy('authority:service_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Service"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Service Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class ServiceDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        service.delete()
        messages.success(request, "Service deleted successfully.")
        return redirect('authority:service_list')

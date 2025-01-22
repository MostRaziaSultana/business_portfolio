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
   ContactMessage
)
from authority.forms import ContactMessageForm

# <<----------------- List, Add, Update, Delete ContactMessage ---------------->>

class ContactMessageListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = ContactMessage
    template_name = 'contact/contact_message_list.html'
    context_object_name = 'contact_messages'
    paginate_by = 10

    def get_queryset(self):
        return ContactMessage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Message List'
        return context


class ContactMessageDetailView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = ContactMessage
    template_name = 'contact/contact_message_detail.html'
    context_object_name = 'contact_message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Message Detail'
        return context


class ContactMessageDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        contact_message = get_object_or_404(ContactMessage, pk=pk)
        contact_message.delete()
        messages.success(request, "Contact message deleted successfully.")
        return redirect('authority:contact_message_list')

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Import Models
from home.models import AboutUs,AboutUsContent

from authority.forms import AboutUsForm,AboutUsContentForm

# <<----------------- List, Add, Update, Delete AboutUs ---------------->>

# AboutUs Views
class AboutUsListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = AboutUs
    template_name = 'about_us/about_us_list.html'
    context_object_name = 'about_data'

    def get_queryset(self):
        return AboutUs.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us List'
        return context


class UpdateAboutUsView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = AboutUs
    form_class = AboutUsForm
    template_name = 'about_us/add_update_about_us.html'
    success_url = reverse_lazy('authority:about_us_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update About Us"
        context["updated"] = True
        return context

    def form_valid(self, form):
        messages.success(self.request, "About Us Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class AddAboutUsView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = AboutUs
    form_class = AboutUsForm
    template_name = 'about_us/add_update_about_us.html'
    success_url = reverse_lazy('authority:about_us_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add About Us"
        return context

    def form_valid(self, form):
        messages.success(self.request, "About Us Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class AboutUsDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        about_us = get_object_or_404(AboutUs, pk=pk)
        about_us.delete()
        messages.success(request, "About Us deleted successfully.")
        return redirect('authority:about_us_list')


# <<----------------- List, Add, Update, Delete AboutUs Content ---------------->>
class AboutUsContentListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = AboutUsContent
    template_name = 'about_us/about_us_content_list.html'
    context_object_name = 'about_us_content_list'

    def get_queryset(self):
        return AboutUsContent.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us Content List'
        return context


class UpdateAboutUsContentView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = AboutUsContent
    form_class = AboutUsContentForm
    template_name = 'about_us/add_update_about_us_content.html'
    success_url = reverse_lazy('authority:about_us_content_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update About Us Content"
        context["updated"] = True
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class AddAboutUsContentView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = AboutUsContent
    form_class = AboutUsContentForm
    template_name = 'about_us/add_update_about_us_content.html'
    success_url = reverse_lazy('authority:about_us_content_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add About Us Content"
        return context

    def form_valid(self, form):
        messages.success(self.request, "About Us Content Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class AboutUsContentDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        about_us_content = get_object_or_404(AboutUsContent, pk=pk)
        about_us_content.delete()
        messages.success(request, "About Us Content deleted successfully.")
        return redirect('authority:about_us_content_list')

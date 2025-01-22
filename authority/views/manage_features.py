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
   Feature,FeatureIcon
)
from authority.forms import FeatureForm,FeatureIconForm

# <<----------------- List, Add, Update, Delete Features ---------------->>

class FeaturesListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Feature
    template_name = 'features/features_list.html'
    context_object_name = 'features_list'

    def get_queryset(self):
        return Feature.objects.order_by('-title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Why choose us List"
        return context


class UpdateFeatureView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Feature
    form_class = FeatureForm
    template_name = 'features/add_update_features.html'
    success_url = reverse_lazy('authority:feature_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        context["updated"] = True
        return context

    def form_valid(self, form):
        messages.success(self.request, "Defination Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class AddFeatureView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Feature
    form_class = FeatureForm
    template_name = 'features/add_update_features.html'
    success_url = reverse_lazy('authority:feature_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Defination  Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)

class FeatureDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        feature = get_object_or_404(Feature, pk=pk)
        feature.delete()
        messages.success(request, "Why choose us deleted successfully.")
        return redirect('authority:feature_list')


# <<----------------- List, Add, Update, Delete FeatureIcon ---------------->>
class FeatureIconListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = FeatureIcon
    template_name = 'features/feature_icon_list.html'
    context_object_name = 'feature_icon_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Icon List"
        return context


class AddFeatureIconView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = FeatureIcon
    form_class = FeatureIconForm
    template_name = 'features/add_update_feature_icon.html'
    success_url = reverse_lazy('authority:feature_icon_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Icon"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Feature Icon added successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class UpdateFeatureIconView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = FeatureIcon
    form_class = FeatureIconForm
    template_name = 'features/add_update_feature_icon.html'
    success_url = reverse_lazy('authority:feature_icon_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Icon"
        context["updated"] = True
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class FeatureIconDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        feature_icon = get_object_or_404(FeatureIcon, pk=pk)
        feature_icon.delete()
        messages.success(request, "Feature Icon deleted successfully.")
        return redirect('authority:feature_icon_list')
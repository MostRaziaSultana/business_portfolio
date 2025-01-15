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
   CarouselItem
)
from authority.forms import CarouselItemForm

# <<----------------- List, Add, Update, Delete Carousel ---------------->>

class CarouselItemListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = CarouselItem
    template_name = 'carousel/carousel_item_list.html'
    context_object_name = 'carousel_items'

    def get_queryset(self):
        return CarouselItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Carousel Item List'
        return context


class AddCarouselItemView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = CarouselItem
    form_class = CarouselItemForm
    template_name = 'carousel/add_update_carousel_item.html'
    success_url = reverse_lazy('authority:carousel_item_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Banner"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Banner Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class UpdateCarouselItemView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = CarouselItem
    form_class = CarouselItemForm
    template_name = 'carousel/add_update_carousel_item.html'
    success_url = reverse_lazy('authority:carousel_item_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Banner"
        return context
    def form_valid(self, form):
        messages.success(self.request, "Banner Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class CarouselItemDeleteView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):

    def post(self, request, pk):
        carousel_item = get_object_or_404(CarouselItem, pk=pk)
        carousel_item.delete()
        messages.success(request, "Banner deleted successfully.")
        return redirect('authority:carousel_item_list')

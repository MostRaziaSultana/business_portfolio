from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404, redirect

# Import Models
from home.models import (
   Product,ProductCategory
)
from authority.forms import ProductForm,ProductCategoryForm

# <<----------------- List, Add, Update, Delete Category ---------------->>


class ProductCategoryListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = ProductCategory
    template_name = 'product/product_category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return ProductCategory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category List'
        return context

class AddProductCategoryView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'product/add_update_category.html'
    success_url = reverse_lazy('authority:product_category_list')

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

class UpdateProductCategoryView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'product/add_update_category.html'
    success_url = reverse_lazy('authority:product_category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Category"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Category Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)

class DeleteProductCategoryView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        product_category = get_object_or_404(ProductCategory, pk=pk)
        product_category.delete()
        messages.success(request, "Category deleted successfully.")
        return redirect('authority:product_category_list')




# <<----------------- List, Add, Update, Delete Product ---------------->>
class ProductListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product List'
        return context

class AddProductView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_update_product.html'
    success_url = reverse_lazy('authority:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Product'
        return context

    def form_valid(self, form):
        messages.success(self.request, "Product added successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)

class UpdateProductView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_update_product.html'
    success_url = reverse_lazy('authority:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Product'
        return context

    def form_valid(self, form):
        messages.success(self.request, "Product updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong, please try again!")
        return super().form_invalid(form)


class DeleteProductView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect('authority:product_list')

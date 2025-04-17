from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Owner
from .forms import OwnerForm

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

# Owner Views
class OwnerListView(ListView):
    model = Owner
    template_name = 'main/owner_list.html'
    context_object_name = 'owners'
    paginate_by = 10

class OwnerDetailView(DetailView):
    model = Owner
    template_name = 'main/owner_detail.html'
    context_object_name = 'owner'

class OwnerCreateView(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'main/owner_form.html'
    success_url = reverse_lazy('owner_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Owner'
        context['button_text'] = 'Create Owner'
        return context

class OwnerUpdateView(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'main/owner_form.html'
    success_url = reverse_lazy('owner_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Owner'
        context['button_text'] = 'Update Owner'
        return context

class OwnerDeleteView(DeleteView):
    model = Owner
    template_name = 'main/owner_confirm_delete.html'
    success_url = reverse_lazy('owner_list')

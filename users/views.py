
from django.shortcuts import render
from django.views import generic
from .forms import NewUserForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = NewUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('products:categories')
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic import CreateView
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(CreateView):
    model = User
    template_name = "users/register.html"
    form_class = RegisterForm
    
    
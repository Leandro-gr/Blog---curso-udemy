from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . forms import UserCreationFromWithEmail

class SignUpView(CreateView):
    form_class = UserCreationFromWithEmail
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from .forms import UserForm
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class SignUpPage(CreateView):
	form_class = UserForm
	template_name = 'registration/signup.html'
	success_url = reverse_lazy('login')


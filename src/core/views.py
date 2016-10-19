from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import dish

# Create your views here.

class main_view(TemplateView):

    template_name = 'main.html'
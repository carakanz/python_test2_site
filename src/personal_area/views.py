from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DeleteView
from .models import user

# Create your views here.

class main_user_view(DeleteView):

    template_name = 'user.html'
from django.conf.urls import url
from django.contrib import admin
from .views import main_view

urlpatterns = [
    url(r'^$', main_view.as_view())
]
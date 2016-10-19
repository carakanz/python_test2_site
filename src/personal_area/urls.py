from django.conf.urls import url
from django.contrib import admin
from .views import main_user_view

urlpatterns = [
    url(r'^$', main_user_view.as_view())
]
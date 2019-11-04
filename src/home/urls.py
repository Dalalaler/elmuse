from django.urls import path

from . import views

urlpatterns = [
    path("", views.elmuse, name='elmuse'),
]
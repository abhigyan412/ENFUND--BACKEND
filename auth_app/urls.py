from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.google_login, name="google_login"),
    path("callback/", views.google_callback, name="google_callback"),
]

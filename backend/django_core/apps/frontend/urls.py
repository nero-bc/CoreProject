from django.urls import re_path

from . import views

urlpatterns = [
    re_path("^animecore/(?:.*)/?$", views.animecore, name="animecore_frontend"),
]
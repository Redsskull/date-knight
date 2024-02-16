from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("date_ideas/", views.date_ideas, name="date_ideas"),
]

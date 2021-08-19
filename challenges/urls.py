from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.number_challenge),
    path("<str:month>", views.month_challenge, name="month-challenge"),
]

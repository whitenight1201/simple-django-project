from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("members/", views.members, name="members"),
    path("members/details/<slug:slug>", views.details, name="details"),
    path("testing/", views.testing, name="testing"),
    path("setcookie", views.setcookie),
    path("getcookie", views.showcookie),
    path("update", views.updating_cookie),
    path("delete", views.deleting_cookie),
]

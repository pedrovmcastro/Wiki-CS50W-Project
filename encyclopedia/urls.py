from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/<str:entry_title>", views.entry_page, name="entry_page")
]

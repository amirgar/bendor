from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/upload/", views.upload_file, name="upload_file"),
]
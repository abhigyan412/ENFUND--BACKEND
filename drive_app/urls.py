from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_file, name="upload_file"),
    path("files/", views.list_files, name="list_files"),
    path("download/<str:file_id>/", views.download_file, name="download_file"),
    path("debug/session/", views.debug_session, name="debug_session"),
]

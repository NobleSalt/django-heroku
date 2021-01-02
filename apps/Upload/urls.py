from django.urls import path
from apps.Upload.views import UploadFile,ListFile

app_name = 'upload'
urlpatterns = [
    path("", ListFile.as_view(), name="files"),
    path("upload/", UploadFile.as_view(), name="home"),
]

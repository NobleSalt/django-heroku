from django.urls import path
from apps.Upload.views import UploadFile,ListFile

app_name = 'upload'
urlpatterns = [
    path("upload/", UploadFile.as_view(), name="home"),
    path("files/", ListFile.as_view(), name="files")
]

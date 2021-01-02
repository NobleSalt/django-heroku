from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FileUpload(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_files')
    main_file = models.FileField(upload_to='files')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    __str__ = lambda self: self.main_file.name

    class Meta:
        ordering = ['-date_uploaded']
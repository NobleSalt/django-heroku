from django import forms
from apps.Upload.models import FileUpload

class UploadForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = '__all__'
from django.shortcuts import render,redirect
from django.views.generic import View

from apps.Upload.forms import UploadForm
from apps.Upload.models import FileUpload


# Create your views here.
class UploadFile(View):
    template_name = 'upload.html'
    # form_class = UploadForm

    get = lambda self, *args, **kwargs : render(self.request, self.template_name, context={'form':UploadForm()})

    def post(self, *args, **kwargs):
        form = UploadForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload:files")
        return render(self.request, self.template_name)


class ListFile(View):
    template_name = 'list.html'
    # form_class = UploadForm

    def get(self, *args, **kwargs):
        files = FileUpload.objects.all()

        return render(self.request, self.template_name, context={'files': files})

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import View
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views import generic

from Finance.models import ReceiptData
from Finance.forms import UploadForm
from Finance.render import Render

def home(request):
    return render(request, 'index.html')

def uploadView(request):
            form = UploadForm(request.POST or None, request.FILES or None)
            #form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                upload = form.save(commit=False)
                upload.save()
                return render(request, 'index.html')
            form = UploadForm()
            return render(request, 'upload.html', {'form': form})

class Pdf(View):

    def get(self, request):
        sales = ReceiptData.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request
        }
        return Render.render('pdf.html', params)

#class AdminSignUpView()
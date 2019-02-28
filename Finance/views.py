from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import View
from Finance.pdf_extract import extract
from Finance.models import ReceiptData
from Finance.forms import UploadForm
from Finance.render import Render
from Finance.utils import send_receipt_message


def home(request):
    return render(request, 'index.html')

def uploadView(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        upload = form.save(commit=False)
        var = request.FILES['document'].name
        if var:
            filename = var
            if filename.endswith('.jpg'):
                print('File is a jpg')
                upload.save()
            elif filename.endswith('.pdf'):
                print('File is a pdf')
                upload.save()
                extract(request)
            elif filename.endswith('.zip'):
                print('File is a zip')
                upload.save()
            else:
                print('File is NOT in correct format')
                form = UploadForm()
                return render(request, 'upload.html', {'form': form})
                # raise form.ValidationError("File is not in format. Please upload only jpg,pdf,zip files")
        send_receipt_message()
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
# class AdminSignUpView()

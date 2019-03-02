from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth import authenticate, login
from Finance import settings
from Finance.pdf_extract import extract, extract_image, extract_zip, extract_image_zip
from Finance.models import ReceiptData, Items, Customer, Uploads
from Finance.forms import UploadForm
from Finance.render import Render
import pdfkit, datetime, os
from zipfile import ZipFile
from django.core.files.base import ContentFile


def home(request):

    items1 = Items.objects.all()
    for x in items1:
        print(x.item_name)
    return render(request, 'index.html')

@login_required()
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
                extract_image(request)
            elif filename.endswith('.pdf'):
                print('File is a pdf')
                upload.save()
                extract(request)
            elif filename.endswith('.zip'):
                print('File is a zip')
                with ZipFile(upload.document) as zip_file:
                    names = zip_file.namelist()
                    for n in names:
                        with zip_file.open(n) as myfile:
                            up = Uploads()
                            up.description = n
                            up.document.save(n, ContentFile(myfile.read()))
                            # fyl = up.document
                            if n.endswith('.pdf'):
                                extract_zip(n)
                            elif n.endswith('.jpg'):
                                extract_image_zip(n)
                            else:
                                print('File is NOT in correct format')
                                form = UploadForm()
                                return render(request, 'upload.html', {'form': form})
                                raise form.ValidationError(
                                    "File is not in format. Please upload only jpg,pdf,zip files")
            else:
                print('File is NOT in correct format')
                form = UploadForm()
                return render(request, 'upload.html', {'form': form})
                raise form.ValidationError("File is not in format. Please upload only jpg,pdf,zip files")
        path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        now = datetime.datetime.now()
        receipt = ReceiptData.objects.last()
        item = Items.objects.filter(invoice_no=receipt.invoice_no)
        context = {
            # 'receipt_no': receipt.invoice_no,
            # 'receipt_amount': receipt.amount,
            # 'receipt_customer': receipt.,
            'receipt': receipt,
            'item': item,
            'today': now.strftime("%d-%m-%Y"),
        }
        print(receipt.invoice_no)
        print(item)
        print(receipt.amount)
        print(type(item))
        template = get_template('pdf.html')
        # c = Context(context)
        html = template.render(context)
        options = {
            'page-size': 'Letter',
            'encoding': "UTF-8",
        }
        filename = receipt.invoice_no
        file_path = os.path.join("pdf\%s.pdf" % filename)
        pdf = pdfkit.from_string(html, file_path, options, configuration=config)
        # response = HttpResponse(pdf, content_type='application/pdf')
        # filename = request.user.username + randint(1, 10000)
        # response['Content-Disposition'] = 'attachment; filename = ""'
        recipients = []
        for user in Customer.objects.all():
            recipients.append(user.customer_email)

        email = EmailMessage(subject='Finance Receipt', body='PFA finance receipt', from_email=settings.EMAIL_HOST_USER,
                             to=recipients)
        email.attach_file(file_path)
        email.send()
        return render(request, 'index.html')
    form = UploadForm()
    return render(request, 'upload.html', {'form': form})

def loginview(request):
    global user
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(request, 'index.html')
            else:
                return render(request, 'registration/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    return redirect(request, 'index.html')

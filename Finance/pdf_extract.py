import PyPDF2
from Finance.nlp import nlp


def extract(request):
    file = request.FILES['document']
    pdf = PyPDF2.PdfFileReader(file)
    text = ''
    for page in pdf.pages:
        text = page.extractText()
    print(text)
    nlp(text)

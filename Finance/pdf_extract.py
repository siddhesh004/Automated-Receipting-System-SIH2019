import PyPDF2
from Finance.nlp import nlp
from tika import parser


def extract(request):
    file = request.FILES['document'].name

    name = str(file)
    finalpath = "templates\\Media\\"+name
    print(finalpath)
    '''
    pdf = PyPDF2.PdfFileReader(file)
    text = ''
    for page in pdf.pages:
        text = page.extractText()
   '''
    raw = parser.from_file(finalpath)
    print(raw['content'])

    nlp(raw['content'])
import PyPDF2
from Finance.nlp import nlp
from tika import parser
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from PIL import Image
#    import numpy as np


pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"


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

def extract_image(request):

    file = request.FILES['document']

    name = str(file)
    finalpath = "templates\\Media\\" + name
    image = cv2.imread(finalpath)
    image = cv2.resize(image, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 23, 10)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang="eng")
    os.remove(filename)
    print(text)
    nlp(text)



import PyPDF2

from Finance.models import User
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


def extract(name, request):

    logger = request.user
    comp = logger.company_name.company_name

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

    return nlp(request,raw['content'],comp,name)

def extract_image(name, request):


    file = request.FILES['document']
    logger = request.user
    comp = logger.company_name.company_name
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
    return nlp(request,text,comp,name)


def extract_zip(name,request):
    logger = request.user
    comp = logger.company_name.company_name
    print(name)
    finalpath = "templates\\Media\\" + name
    print(finalpath)
    raw = parser.from_file(finalpath)
    print(raw['content'])
    return nlp(request,raw['content'],comp,name)


def extract_image_zip(name,request):

    logger = request.user
    comp = logger.company_name.company_name
    finalpath = "templates\\Media\\" + name
    image = cv2.imread(finalpath)
    #image = cv2.resize(image, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 23, 10)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)
        text = pytesseract.image_to_string(Image.open(filename), lang="eng")
        os.remove(filename)

        print(text)
        return nlp(request,text,comp,name)

def extract_file(filename):
    logger = "siddhesh"
    comp = User.objects.get(username=logger)
    comp = comp.company_name.company_name
    # print ("---------------------------------------"+comp.dtype+"----------------------------------------")
    raw = parser.from_file("templates\\Media\\" + filename)
    print(raw['content'])
    nlp(raw['content'], comp)

def extract_image_file(filename):
    # file = request.FILES['document']
    logger = "siddhesh"
    comp = User.objects.get(username=logger)
    comp = comp.company_name.company_name
    finalpath = "templates\\Media\\" + filename
    image = cv2.imread(finalpath)
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 23, 10)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang="eng")
    print(text)
    nlp(text, comp)
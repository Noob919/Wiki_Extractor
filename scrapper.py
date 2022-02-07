#Required Libaries
from distutils.command import config
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
import json

#Function to convert pdf file to image
def pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

#Function to extract text from image
def convert_img_to_txt(file):
    text = image_to_string(file, lang = 'mar')
    return text


#Function to take pdf file and return text from the file in string.
def get_txt_from_any_pdf(pdf_file):
    images  = pdf_to_img(pdf_file=pdf_file)
    final = ""
    for pg,img in enumerate(images):
        final += convert_img_to_txt(img)
    
    return final

#File path
path_to_pdf = "6-historry.pdf"


plain_txt = get_txt_from_any_pdf(path_to_pdf)

#Dictionary to dump in jason
pdf_dict = {"page-url": path_to_pdf, "pdf-url": path_to_pdf, "content of the pdf": plain_txt}
# print(pdf_dict)


with open('pdf_extract.json','a') as fp:
        json.dump(pdf_dict,fp,indent =20, ensure_ascii=True)
        fp.close()
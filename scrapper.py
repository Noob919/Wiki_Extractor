from distutils.command import config
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
import json
# my_config = r"-l hin "
def pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

def convert_img_to_txt(file):
    text = image_to_string(file, lang = 'mar')
    return text

def get_txt_from_any_pdf(pdf_file):
    images  = pdf_to_img(pdf_file=pdf_file)
    final = ""
    for pg,img in enumerate(images):
        final += convert_img_to_txt(img)
    
    return final

path_to_pdf = "12-std-political-marathi.pdf"
plain_txt = get_txt_from_any_pdf(path_to_pdf)
pdf_dict = {"page-url": path_to_pdf, "pdf-url": path_to_pdf, "content of the pdf": plain_txt}
# print(pdf_dict)

with open('data.json','a') as fp:
        json.dump(pdf_dict,fp,indent =20, ensure_ascii=True)
        fp.close()
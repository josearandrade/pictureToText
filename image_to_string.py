import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import numpy as np

def aplicar_mascaras(imagem):
    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    img = cv2.bilateralFilter(imagem_cinza, 7, 75, 75)
    _, img_bin = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    _, img_otsu = cv2.threshold(img_bin, 0, 255, cv2.THRESH_OTSU)
    return img_otsu

def imagem_para_texto(caminho_imagem):
    
    imagem = Image.open(caminho_imagem)
    # Converter a imagem em texto usando o pytesseract
    texto = pytesseract.image_to_string(imagem, lang='por', config='--psm 6') 
    return texto

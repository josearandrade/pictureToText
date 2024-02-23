import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import numpy as np

def aplicar_mascaras(imagem):
    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    img = cv2.bilateralFilter(imagem_cinza, 7, 75, 75)
    
    # Aplicar filtro de suavização (filtro gaussiano)
    #imagem_suavizada = cv2.GaussianBlur(img, (5, 5), 0)
    
    _, img_bin = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

    _, img_otsu = cv2.threshold(img_bin, 0, 255, cv2.THRESH_OTSU)
    # Aplicar binarização
   # _, imagem_binaria = cv2.threshold(imagem_suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return img_otsu

# Carregar a imagem
imagem = cv2.imread('images/anajunto.png')

# Aplicar máscaras
imagem_processada = aplicar_mascaras(imagem)

# Salvar a imagem processada
cv2.imwrite('images/imagem_processada.png', imagem_processada) 

# Exibir a imagem processada
#cv2.imshow('Imagem Processada', imagem_processada)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


def imagem_para_texto(caminho_imagem):
    # Abrir a imagem usando PIL (Python Imaging Library)
    imagem = Image.open(caminho_imagem)
    # Converter a imagem em texto usando o pytesseract
    texto = pytesseract.image_to_string(imagem, lang='por', config='--psm 6') 
    return texto

# Caminho da imagem que você deseja converter em texto
caminho_imagem = "images/imagem_processada.png"

# Chamada da função para converter a imagem em texto
texto_convertido = imagem_para_texto(caminho_imagem)

# Exibir o texto convertido
print(texto_convertido)

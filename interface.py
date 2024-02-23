import tkinter as tk
from tkinter import filedialog
from image_to_string import *
from PIL import Image, ImageTk
import shutil

def enviar_arquivo():
    filename = filedialog.askopenfilename()
    if filename:
        # Copia o arquivo para um novo local
        novo_local = "images/imagem.png" 
        shutil.copy(filename, novo_local)
        imagem = cv2.imread('images/imagem.png')
        imagem_processada = aplicar_mascaras(imagem)
        cv2.imwrite('images/imagem_processada.png', imagem_processada)

def converter_imagem_para_texto():
    filename = "images/imagem_processada.png"
    if filename:
        texto = imagem_para_texto(filename)
        caixa_texto.insert(tk.END, texto)
        
def copiar_texto():
    texto_selecionado = caixa_texto.selection_get()
    janela.clipboard_clear()
    janela.clipboard_append(texto_selecionado)

# Aplicar máscaras
imagem_processada = aplicar_mascaras(imagem)

# Salvar a imagem processada
cv2.imwrite('images/imagem_processada.png', imagem_processada) 

root = tk.Tk()

root.title("Foto para texto")
# Definir o tamanho da janela (largura x altura)
largura_janela = 400
altura_janela = 200
root.geometry(f"{largura_janela}x{altura_janela}")

# Botão para enviar arquivo
botao_enviar = tk.Button(root, text="Enviar Arquivo", command=enviar_arquivo)
botao_enviar.pack()

# Botão para chamar a função imagem_para_texto
botao_converter = tk.Button(root, text="Converter Imagem para Texto", command=converter_imagem_para_texto)
botao_converter.pack()

# Label para exibir informações
label_imagem = tk.Label(root, text="")
label_imagem.pack()

# Criar uma caixa de texto
caixa_texto = tk.Text(root, height=10, width=50)
caixa_texto.pack()


root.mainloop()

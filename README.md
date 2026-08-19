# pictureToText

Aplicação desktop simples para extrair texto de imagens usando OCR (*Optical Character Recognition*). O projeto foi desenvolvido para a disciplina de **Informática Biomédica na Atenção à Saúde 2**.

O aplicativo permite selecionar uma imagem, aplicar um pré-processamento para facilitar a leitura e converter seu conteúdo em texto em português.

## Funcionalidades

- Seleção de imagem por janela de arquivos.
- Cópia da imagem escolhida para a pasta `images/`.
- Conversão para escala de cinza, filtro bilateral e binarização com OpenCV.
- Reconhecimento de texto em português com Tesseract OCR.
- Exibição do texto reconhecido em uma interface gráfica Tkinter.

## Tecnologias

- Python 3
- Tkinter
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [pytesseract](https://pypi.org/project/pytesseract/)
- OpenCV
- Pillow
- NumPy

## Pré-requisitos

1. Instale o Python 3.
2. Instale o Tesseract OCR.
3. Durante a instalação do Tesseract, inclua o pacote de idioma português (`por`).
4. Instale as dependências Python:

```powershell
python -m pip install pytesseract opencv-python Pillow numpy
```

Por padrão, o projeto procura o executável do Tesseract neste caminho do Windows:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Se ele estiver instalado em outro local, atualize a variável `tesseract_cmd` em `image_to_string.py`.

## Como executar

No diretório do projeto, execute:

```powershell
python interface.py
```

Na janela aberta:

1. Clique em **Enviar Arquivo** e escolha uma imagem.
2. Clique em **Converter Imagem para Texto**.
3. Consulte o resultado na caixa de texto.

## Estrutura do projeto

```text
.
├── interface.py          # Interface gráfica e fluxo de seleção/conversão
├── image_to_string.py    # Pré-processamento e OCR
├── images/               # Imagens de entrada e imagens processadas
└── tesseract_psm.txt     # Referência dos modos de segmentação do Tesseract
```

## Processamento da imagem

Antes do OCR, a imagem passa pelas seguintes etapas:

1. Conversão para tons de cinza.
2. Aplicação de filtro bilateral para reduzir ruído preservando bordas.
3. Binarização por limiar.
4. Binarização de Otsu.

O OCR usa o idioma `por` e o modo de segmentação `--psm 6`, apropriado para blocos uniformes de texto. Outros modos disponíveis estão descritos em `tesseract_psm.txt`.

## Autor

José Augusto Rodrigues de Andrade

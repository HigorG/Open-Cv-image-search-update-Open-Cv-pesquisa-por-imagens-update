import cv2
import numpy as np
import json

# Lê a imagem
imagem = cv2.imread('1.jpg')

# Verifica se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem.")
else:
    # Converte a imagem para escala de cinza
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplica um threshold para binarizar a imagem
    _, imagem_binaria = cv2.threshold(imagem_gray, 127, 255, cv2.THRESH_BINARY)

    # Converte a imagem binarizada em um array de 0s e 1s
    imagem_array = (imagem_binaria // 255).astype(int)

    # Obtem o número de linhas e colunas
    num_linhas, num_colunas = imagem_array.shape

    # Inicializa a lista para armazenar a contagem de pixels pretos em cada linha
    caract = []
    
    # Conta os pixels pretos em cada linha
    for y in range(num_linhas):
        count = 0
        for x in range(num_colunas):
            valor_pixel = imagem_binaria[y, x]
            # Verifica se o valor do pixel é preto (0)
            if valor_pixel == 0:
                count += 1
        caract.append(count)  # Adiciona a contagem da linha atual

    # Mostra o array resultante
    print("Array resultante:")
    print(imagem_array)
    print(f"Número de linhas: {num_linhas}")
    print(f"Número de colunas: {num_colunas}")
    print(caract)

    # Salva o array em um arquivo JSON
    with open('imagem_array.json', 'w') as json_file:
        json.dump(caract, json_file)  # Salva o array de caracteres no JSON

    print("Array salvo em 'imagem_array.json'.")

    # Opcional: Mostra as imagens
    # cv2.imshow('Imagem Original', imagem)
    # cv2.imshow('Imagem Binarizada', imagem_binaria)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
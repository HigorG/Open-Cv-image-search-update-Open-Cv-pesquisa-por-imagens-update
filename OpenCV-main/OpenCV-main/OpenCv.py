import cv2
import numpy as np

# Carregar a imagem usando o caminho fornecido
imagem = cv2.imread()

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro: A imagem não pôde ser carregada. Verifique o caminho.")
else:
    # Definir as dimensões máximas
    largura_maxima = 800
    altura_maxima = 600
    
    # Obter as dimensões da imagem original
    altura, largura = imagem.shape[:2]

    # Calcular a proporção de redimensionamento
    proporcao = min(largura_maxima / largura, altura_maxima / altura)

    # Calcular novas dimensões mantendo a proporção
    nova_largura = int(largura * proporcao)
    nova_altura = int(altura * proporcao)

    # Redimensionar a imagem
    imagem_redimensionada = cv2.resize(imagem, (nova_largura, nova_altura))

    # Cortar a imagem na vertical (lado esquerdo)
    imagem_cortada = imagem_redimensionada[:, :nova_largura // 2]

    # Função para encontrar todas as características do objeto
    def encontrar_caracteristicas(imagem):
        # Converter a imagem para escala de cinza
        gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        
        # Aplicar um desfoque para reduzir ruídos
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Aplicar um limiar para binarizar a imagem
        _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

        # Encontrar contornos
        contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Lista para armazenar características
        caracteristicas = []

        # Se contornos forem encontrados
        if contornos:
            for contorno in contornos:
                # Obter o ponto mais à esquerda (ponta) e o ponto mais à direita (costa)
                ponta = tuple(contorno[contorno[:, :, 0].argmin()][0])
                costa = tuple(contorno[contorno[:, :, 0].argmax()][0])
                
                # Calcular a distância entre a ponta e a costa
                distancia = np.linalg.norm(np.array(ponta) - np.array(costa))
                
                # Adicionar as características à lista
                caracteristicas.append({
                    'ponta': ponta,
                    'costa': costa,
                    'distancia': distancia
                })
                
                # Desenhar os contornos e os pontos na imagem
                cv2.drawContours(imagem, [contorno], -1, (0, 255, 0), 2)
                cv2.circle(imagem, ponta, 5, (255, 0, 0), -1)  # Ponta
                cv2.circle(imagem, costa, 5, (0, 0, 255), -1)  # Costa
            
            # Exibir a imagem com as características
            cv2.imshow("Imagem com Características", imagem)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            return caracteristicas
        else:
            print("Nenhum contorno encontrado.")
            return []

    # Chamar a função na imagem cortada
    caracteristicas = encontrar_caracteristicas(imagem_cortada)

    # Exibir todas as características encontradas
    for i, caracteristica in enumerate(caracteristicas):
        print(f"Característica {i + 1}: Ponta: {caracteristica['ponta']}, "
              f"Costa: {caracteristica['costa']}, Distância: {caracteristica['distancia']:.2f} pixels")
        

# nao cortar a imagem
# usar for para percorrer a matrix para correr nas colunos e em  seguida para percorrer as linhas
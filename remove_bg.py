from PIL import Image
import numpy as np

# Carregar a imagem
img = Image.open('Logo.jpg')
img = img.convert("RGBA")

# Converter para array numpy
data = np.array(img)

# Obter as dimensões
height, width = data.shape[:2]

# Encontrar o centro da imagem
center_x, center_y = width // 2, height // 2

# Calcular o raio do círculo (aproximadamente 45% da largura)
radius = min(width, height) * 0.47

# Criar máscara para preservar apenas o círculo
for y in range(height):
    for x in range(width):
        # Calcular distância do pixel ao centro
        distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
        
        # Se o pixel está fora do círculo, tornar transparente
        if distance > radius:
            data[y, x] = [0, 0, 0, 0]  # Transparente
        else:
            # Se está dentro do círculo, verificar se é branco e remover
            r, g, b, a = data[y, x]
            # Se for muito branco (próximo de 255,255,255), tornar transparente
            if r > 240 and g > 240 and b > 240:
                data[y, x] = [0, 0, 0, 0]

# Criar nova imagem
img_final = Image.fromarray(data, 'RGBA')

# Salvar como PNG com transparência
img_final.save('logo_transparente.png', 'PNG')
print("Logo salva com sucesso como logo_transparente.png!")

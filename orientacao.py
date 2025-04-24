import cv2
import pytesseract
import os
from pytesseract import Output

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Pastas
origem = "original_images"
saida = "processed_images"
os.makedirs(saida, exist_ok=True)

# Função para adicionar texto na imagem
def escrever(img, texto):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    return cv2.putText(img, texto, (10, 30), fonte, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

# Função para ajustar brilho e contraste (simples)
def ajustar_brilho_contraste(img, alpha=1.5, beta=20):
    return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# OCR confiabilidade
def ocr_confidence(image):
    data = pytesseract.image_to_data(image, output_type=Output.DICT)
    confidences = [int(conf) for conf in data['conf'] if conf != '-1']
    return sum(confidences) / len(confidences) if confidences else 0

def rotate_image(image, angle):
    if angle == 0:
        return image
    elif angle == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 180:
        return cv2.rotate(image, cv2.ROTATE_180)
    elif angle == 270:
        return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

def processar_imagem(img_path, nome_arquivo):
    img = cv2.imread(img_path)

    # Etapa 1: Redimensionamento
    img_resized = cv2.resize(img, (500, 500))
    img_annotated = escrever(img_resized.copy(), "Redimensionado")
    cv2.imwrite(os.path.join(saida, f"1_redimensionado_{nome_arquivo}"), img_annotated)

    # Etapa 2: Conversão para escala de cinza
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    img_gray_annotated = escrever(cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR), "Convertido para Cinza")
    cv2.imwrite(os.path.join(saida, f"2_cinza_{nome_arquivo}"), img_gray_annotated)

    # Etapa 3: Ajuste de brilho/contraste
    img_bc = ajustar_brilho_contraste(img_resized)
    img_bc_annotated = escrever(img_bc.copy(), "Brilho/Contraste Ajustado")
    cv2.imwrite(os.path.join(saida, f"3_brilho_contraste_{nome_arquivo}"), img_bc_annotated)

    # Etapa 4: Correção de orientação
    melhor_conf = 0
    melhor_img = img_bc
    melhor_angulo = 0
    for angle in [0, 90, 180, 270]:
        rotacionada = rotate_image(cv2.cvtColor(img_bc, cv2.COLOR_BGR2GRAY), angle)
        conf = ocr_confidence(rotacionada)
        if conf > melhor_conf:
            melhor_conf = conf
            melhor_img = rotate_image(img_bc, angle)
            melhor_angulo = angle

    final = escrever(melhor_img.copy(), f"Corrigida Rotação {melhor_angulo}°")
    cv2.imwrite(os.path.join(saida, f"4_orientada_{nome_arquivo}"), final)
    print(f"{nome_arquivo} finalizado com rotação {melhor_angulo}°")

# Rodar para todas as imagens
for arquivo in os.listdir(origem):
    if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
        caminho = os.path.join(origem, arquivo)
        processar_imagem(caminho, arquivo)


for arquivo in os.listdir(origem):
    if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
        caminho = os.path.join(origem, arquivo)
        processar_imagem(caminho, arquivo)

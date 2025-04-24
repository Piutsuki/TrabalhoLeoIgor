# 📷 Correção de Orientação em Imagens com OpenCV e Tesseract OCR

## 👨‍💻 Membros do Grupo
- [Igor Do couto maier] – Programação, testes e organização
- [Leonardo] – Pesquisa, testes e apoio no desenvolvimento


## 🎯 Problema Proposto
Durante a análise do dataset de imagens de embalagens de medicamentos, foi identificado que algumas imagens estavam rotacionadas incorretamente (de lado ou de cabeça para baixo), o que dificultava a leitura do conteúdo por humanos e por sistemas automáticos de leitura de texto (OCR).

## 💡 Solução Aplicada
Desenvolvemos uma solução que realiza o pré-processamento das imagens e corrige automaticamente a rotação com base na leitura de texto utilizando OCR (Tesseract). O processo é todo feito com Python e a biblioteca OpenCV.

---

## 📦 Dataset Utilizado

- **Nome:** The Drug Name Detection Dataset  
- **Origem:** Kaggle  
- **Link:** [https://www.kaggle.com/datasets/pkdarabi/the-drug-name-detection-dataset](https://www.kaggle.com/datasets/pkdarabi/the-drug-name-detection-dataset)

---

## 🛠️ Técnicas de Processamento de Imagens Utilizadas

As seguintes etapas foram aplicadas em cada imagem:

1. **Redimensionamento** para tamanho padrão (500x500)
2. **Conversão para escala de cinza** para melhor contraste e leitura
3. **Ajuste de brilho e contraste** com multiplicador e deslocamento
4. **Correção de rotação automática**:
   - A imagem é rotacionada em 4 ângulos (0°, 90°, 180°, 270°)
   - Utiliza o Tesseract OCR para identificar qual rotação possui maior confiança na leitura do texto
   - A imagem é salva com a rotação que oferece maior legibilidade

Cada etapa é salva como imagem separada e **anotada com um texto descritivo**, indicando o processamento realizado.

---

## 🗂️ Estrutura do Projeto

```plaintext
📁 seu-projeto/
├── 📁 original_images/        → Imagens originais a serem processadas
├── 📁 processed_images/       → Imagens processadas com descrições visuais
├── orientacao.py              → Script principal com todo o processamento
└── README.md                  → Este arquivo





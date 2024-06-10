# Projeto de Detecção de Calvície

Este projeto foi desenvolvido para detectar a calvície em imagens usando uma rede neural treinada. A aplicação permite que o usuário selecione uma imagem do computador ou capture uma imagem usando a câmera, e então a rede neural irá analisar a imagem e informar se a pessoa na foto é calva ou não.

## Funcionalidades

- **Selecionar Imagem:** O usuário pode selecionar uma imagem armazenada em seu computador.
- **Capturar Imagem:** O usuário pode capturar uma imagem ao vivo usando a câmera do computador.
- **Detecção de Calvície:** A aplicação analisa a imagem e retorna se a pessoa na foto é calva ou não.

## Como Usar

1. **Executar a Aplicação:**
   - Para executar a aplicação, você precisará ter o Python instalado em seu computador.
   - Instale as dependências necessárias executando o comando:
     ```bash
     pip install -r requirements.txt
     ```
   - Em seguida, execute o arquivo Python principal que contém a interface da aplicação:
     ```bash
     python main.py
     ```

2. **Selecionar ou Capturar Imagem:**
   - Abra a aplicação e clique no botão "Selecionar Imagem e Detectar" para escolher uma imagem do seu computador.
   - Ou clique no botão "Capturar Imagem" para tirar uma foto usando a câmera do seu computador.

3. **Verificar Resultado:**
   - Após selecionar ou capturar a imagem, a aplicação exibirá a imagem e informará se a pessoa na foto é calva ou não.

## Requisitos do Sistema

- Python 3.6 ou superior
- Bibliotecas Python necessárias (listadas em `requirements.txt`)

## Observações

- Este projeto é um exemplo simples de como utilizar redes neurais para detecção de características em imagens.
- A precisão do modelo pode variar dependendo da qualidade das imagens e do treinamento da rede neural.

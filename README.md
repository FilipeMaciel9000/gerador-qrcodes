🔗 Gerador de QR Code com Favicon

Este projeto em Python gera QR Codes para URLs, com a funcionalidade de inserir automaticamente o favicon (ícone) do site no centro. É uma ótima ferramenta para criar QR Codes personalizados e visualmente atraentes para seus projetos ou portfólio.
✨ Funcionalidades

    Geração de QR Code: Cria QR Codes padrão para qualquer URL.

    Favicon Automático: Tenta baixar o favicon do site e o centraliza no QR Code.

    Design Elegante: O favicon é redimensionado para se ajustar perfeitamente ao centro do QR Code.

    Modo de Fallback: Se o favicon não puder ser baixado, um QR Code simples e funcional é gerado.

    Suporte a Múltiplos URLs: O script pode gerar vários QR Codes de uma só vez a partir de um dicionário de sites.

    Organização de Saída: Salva todos os QR Codes em uma pasta output/ para fácil acesso.
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
🛠 Tecnologias Utilizadas

    Python 3: A linguagem principal do projeto.

    qrcode: Biblioteca para a geração do QR Code.

    Pillow (PIL): Usada para manipulação de imagens, como redimensionar e colar o favicon no QR Code.

    requests: Biblioteca para fazer requisições HTTP e baixar o favicon do site.

📦 Instalação e Execução

Siga os passos abaixo para começar a usar o projeto.

    Clone o repositório:

    git clone https://github.com/seuusuario/seuprojeto.git
    cd seuprojeto

    (Opcional) Crie um ambiente virtual:

    python -m venv venv
    # Ative o ambiente virtual
    # Linux/Mac:
    source venv/bin/activate
    # Windows:
    venv\Scripts\activate

    Instale as dependências:
    O arquivo requirements.txt lista todas as bibliotecas necessárias.

    pip install -r requirements.txt

    Execute o script:
    Basta rodar o arquivo principal para gerar os QR Codes.

    python main.py

📂 Estrutura de Saída

Ao executar o script, a pasta output/ será criada com os seguintes arquivos:

📂 output/
├── python.png
├── qrcode_google.png
├── qrcode_github.png
├── qrcode_openai.png
└── qrcode_stackoverflow.png

🖼 Exemplo de Saída

Aqui está um exemplo de como o QR Code final se parece.

Exemplo do QR Code gerado para o site da Python.org
📄 Licença

Este projeto está licenciado sob a MIT License.

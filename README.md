# 🔗 Gerador de QR Code com Favicon

Projeto em Python que gera QR Codes para URLs, inserindo automaticamente o favicon (ícone) do site no centro do QR Code. Uma ferramenta prática para criar QR Codes personalizados, elegantes e visualmente atraentes para seus projetos ou portfólio.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

---

## ✨ Funcionalidades

* **Geração de QR Code:** Cria QR Codes padrão para qualquer URL.
* **Favicon automático:** Baixa o favicon do site e o posiciona no centro do QR Code.
* **Design elegante:** Redimensiona o favicon para se ajustar perfeitamente no QR Code, sem comprometer a leitura.
* **Fallback inteligente:** Caso o favicon não seja encontrado, gera um QR Code simples e funcional.
* **Suporte a múltiplas URLs:** Gera vários QR Codes a partir de um dicionário de sites.
* **Organização da saída:** Salva todos os QR Codes na pasta `output/` para fácil acesso.

---

## 🛠 Tecnologias utilizadas

* **Python 3** — Linguagem principal do projeto.
* **qrcode** — Biblioteca para geração dos QR Codes.
* **Pillow (PIL)** — Manipulação e edição de imagens.
* **requests** — Para realizar requisições HTTP e baixar os favicons.

---

## 📦 Instalação e execução

Siga os passos abaixo para rodar o projeto localmente.

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
```

2. (Opcional) Crie e ative um ambiente virtual:

* Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

* Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o script principal:

```bash
python main.py
```

---

## 📂 Estrutura de saída

Ao rodar o script, será criada a pasta `output/` contendo os arquivos gerados:

```
output/
├── python.png
├── qrcode_google.png
├── qrcode_github.png
├── qrcode_openai.png
└── qrcode_stackoverflow.png
```

---

## 🖼 Exemplo de saída

Abaixo, exemplo do QR Code gerado para o site oficial do Python:

![Exemplo QR Code Python](output/python.png)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

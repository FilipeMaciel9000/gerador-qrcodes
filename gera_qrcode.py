import qrcode
from PIL import Image
import requests
from io import BytesIO
from pathlib import Path
from typing import Dict, Optional

def baixar_favicon(url: str, tamanho: int = 64) -> Optional[Image.Image]:
    """Tenta baixar o favicon de um site."""
    try:
        dominio = url.split('//')[-1].split('/')[0]
        favicon_url = f"https://{dominio}/favicon.ico"
        
        resposta = requests.get(favicon_url, timeout=5)
        resposta.raise_for_status()
        
        favicon = Image.open(BytesIO(resposta.content))
        favicon.thumbnail((tamanho, tamanho))
        return favicon.convert("RGBA")
        
    except Exception as e:
        print(f"⚠️ Não foi possível baixar favicon para {url}: {e}")
        return None

def criar_qrcode_com_favicon(url: str, nome_arquivo: Path) -> None:
    """Cria QR Code com favicon central."""
    try:
        # Configuração do QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Cria a imagem base
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        
        # Tenta baixar e inserir o favicon
        favicon = baixar_favicon(url, tamanho=img.size[0]//4)
        if favicon:
            pos = ((img.size[0] - favicon.size[0]) // 2, (img.size[1] - favicon.size[1]) // 2)
            img.paste(favicon, pos, favicon)
            print(f"✅ QR Code com favicon salvo como {nome_arquivo}")
        else:
            print(f"✅ QR Code simples salvo como {nome_arquivo} (favicon não encontrado)")
            
        img.save(nome_arquivo)
        
    except Exception as e:
        print(f"❌ Erro ao criar QR Code: {e}")

def criar_varios_qrcodes(sites: Dict[str, str], pasta_saida: Path) -> None:
    """Cria vários QR Codes com favicons."""
    for nome, url in sites.items():
        nome_arquivo = pasta_saida / f"qrcode_{nome.lower().replace(' ', '_')}.png"
        criar_qrcode_com_favicon(url, nome_arquivo)

def main():
    pasta_saida = Path("output")
    pasta_saida.mkdir(exist_ok=True)

    # 1️⃣ QR Code com favicon automático
    criar_qrcode_com_favicon("https://www.python.org", pasta_saida / "python.png")

    # 2️⃣ Vários QR Codes
    sites = {
        "Google": "https://www.google.com",
        "GitHub": "https://github.com",
        "OpenAI": "https://openai.com",
        "StackOverflow": "https://stackoverflow.com",
    }
    criar_varios_qrcodes(sites, pasta_saida)

if __name__ == "__main__":
    main()
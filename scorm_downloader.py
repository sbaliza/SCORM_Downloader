#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import requests
from urllib.parse import urljoin, urlparse, unquote
from bs4 import BeautifulSoup
from tqdm import tqdm

def baixar_arquivo(url_arquivo, caminho_local):
    """
    Faz download de um arquivo a partir da URL e salva no caminho especificado.
    """
    try:
        resposta = requests.get(url_arquivo, stream=True, timeout=10)
        resposta.raise_for_status()
        os.makedirs(os.path.dirname(caminho_local), exist_ok=True)
        with open(caminho_local, 'wb') as f:
            for chunk in resposta.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✔ Baixado: {caminho_local}")
    except Exception as e:
        print(f"✖ Erro ao baixar {url_arquivo}: {e}")

def extrair_links_manifesto(url_manifesto):
    """
    Extrai os atributos href do XML de manifesto SCORM.
    """
    try:
        resposta = requests.get(url_manifesto, timeout=10)
        resposta.raise_for_status()
        soup = BeautifulSoup(resposta.content, 'xml')
        links = [tag.get('href') for tag in soup.find_all(href=True)]
        return links
    except Exception as e:
        print(f"✖ Erro ao processar o manifesto: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Downloader de pacotes SCORM via manifesto.")
    parser.add_argument('--manifest', required=True, help='URL do imsmanifest.xml do pacote SCORM')
    parser.add_argument('--output', default=None, help='Diretório base para salvar os arquivos (default: baseado na URL do manifesto)')
    args = parser.parse_args()

    url_manifesto = args.manifest
    print(f"📥 Baixando manifestos de: {url_manifesto}")
    arquivos_href = extrair_links_manifesto(url_manifesto)

    if not arquivos_href:
        print("⚠ Nenhum link encontrado no manifesto.")
        return

    parsed = urlparse(url_manifesto)
    caminho_manifesto_relativo = parsed.path.lstrip('/').rsplit('/', 1)[0]  # ex: cursos/1073_EVG/scorms/modulo01

    # Se o usuário especificou --output, incorporamos a estrutura relativa ao manifesto
    if args.output:
        base_dir = os.path.join(os.path.abspath(args.output), caminho_manifesto_relativo)
    else:
        base_dir = os.path.join(os.getcwd(), caminho_manifesto_relativo)

    base_url = url_manifesto.rsplit('/', 1)[0] + '/'

    for href in tqdm(arquivos_href, desc="🔗 Baixando arquivos"):
        href_decodificado = unquote(href)
        url_arquivo = urljoin(base_url, href)
        caminho_arquivo_local = os.path.join(base_dir, href_decodificado.replace('\\', '/'))
        baixar_arquivo(url_arquivo, caminho_arquivo_local)

if __name__ == "__main__":
    main()
  

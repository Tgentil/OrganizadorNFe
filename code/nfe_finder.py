"""
    Esse script procura por um valor específico em uma lista de notas fiscais
"""
import os
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Especifica o diretório onde estão os arquivos XML
DIRETORIO = "./data"

# Valor específico a ser procurado na tag <vPag>
VALOR_PROCURADO = "518.70"  # Coloque aqui o valor que deseja procurar

# Variável para controlar se o valor foi encontrado
VALOR_ENCONTRADO = False

# Loop pelos arquivos no diretório
for arquivo in os.listdir(DIRETORIO):
    if arquivo.endswith('.xml'):  # Verifica se é um arquivo XML
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(DIRETORIO, arquivo)

        try:
            # Lê o arquivo XML
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()

            # Obtém a tag <vPag>
            tag_vpag = root.find(".//{http://www.portalfiscal.inf.br/nfe}vPag")

            if tag_vpag is not None:
                valor_pagamento = tag_vpag.text

                # Verifica se o valor encontrado é igual ao valor procurado
                if valor_pagamento == VALOR_PROCURADO:
                    print(f"Valor: {VALOR_PROCURADO} , encontrado na nota fiscal: {arquivo}")
                    VALOR_ENCONTRADO = True

        except IOError as e:
            print(f'O arquivo {arquivo} não pôde ser lido: {e}')
            continue  # Pula para o próximo arquivo

# Verifica se o valor foi encontrado
if not VALOR_ENCONTRADO:
    print(f"Valor de pagamento {VALOR_PROCURADO} não encontrado em nenhum arquivo.")

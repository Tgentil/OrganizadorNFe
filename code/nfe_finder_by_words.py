import os
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Especifica o diretório onde estão os arquivos XML
DIRETORIO = "./data"

# Palavras-chave a serem procuradas
PALAVRAS_CHAVE = ["Juros", "juros", "Multa", "multa", "Desconto", "desconto", "Terminal" ]

# Variável para controlar se alguma das palavras-chave foi encontrada
ENCONTRADO = False

# Loop pelos arquivos no diretório
for arquivo in os.listdir(DIRETORIO):
    if arquivo.endswith('.xml'):  # Verifica se é um arquivo XML
        caminho_arquivo = os.path.join(DIRETORIO, arquivo)  # Obtém o caminho completo do arquivo

        try:
            # Lê o arquivo XML
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()

            # Convertendo o XML em uma string para facilitar a busca por palavras
            xml_string = ET.tostring(root, encoding='utf-8').decode('utf-8')

            # Verifica se alguma das palavras-chave está presente no conteúdo do XML
            if any(palavra in xml_string for palavra in PALAVRAS_CHAVE):
                print(f"Palavras-chave encontradas na nota fiscal: {arquivo}")
                ENCONTRADO = True

        except IOError as e:
            print(f'O arquivo {arquivo} não pôde ser lido: {e}')
            continue  # Pula para o próximo arquivo

# Verifica se alguma palavra-chave foi encontrada
if not ENCONTRADO:
    print("Nenhuma das palavras-chave foi encontrada em nenhum arquivo.")

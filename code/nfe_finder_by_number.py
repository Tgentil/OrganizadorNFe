"""
    Esse script procura notas fiscais cujos números estão especificados em um array e move os arquivos encontrados para uma pasta de saída.
"""
import os
import shutil
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Especifica o diretório onde estão os arquivos XML
DIRETORIO = "./data"
# Especifica o diretório de saída
DIRETORIO_SAIDA = "./out"

# Cria o diretório de saída se ele não existir
if not os.path.exists(DIRETORIO_SAIDA):
    os.makedirs(DIRETORIO_SAIDA)

# Array com os números das notas fiscais a serem procurados
NUMEROS_NOTAS = ["38998", "38977", "38967", "35482", "39045", "39049", "38979", "39020",
                "39019", "38981", "38995", "39035", "38988", "39014", "38970", "39044",
                "39023", "38961", "39038"]

# Dicionário para acompanhar notas encontradas
notas_encontradas = {nota: False for nota in NUMEROS_NOTAS}

print("Script iniciado.")

# Loop pelos arquivos no diretório
for arquivo in os.listdir(DIRETORIO):
    if arquivo.endswith('.xml'):  # Verifica se é um arquivo XML
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(DIRETORIO, arquivo)

        try:
            # Lê o arquivo XML
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()

            # Obtém a tag <nNF> que contém o número da nota fiscal
            tag_nnf = root.find(".//{http://www.portalfiscal.inf.br/nfe}nNF")

            if tag_nnf is not None:
                numero_nota = tag_nnf.text

                # Verifica se o número da nota está no array e marca como encontrado
                if numero_nota in NUMEROS_NOTAS:
                    notas_encontradas[numero_nota] = True
                    # Move o arquivo para a pasta de saída
                    shutil.move(caminho_arquivo, os.path.join(DIRETORIO_SAIDA, arquivo))

        except ET.ParseError as e:
            print(f"Erro de parse no arquivo {arquivo}: {e}")
        except IOError as e:
            print(f'O arquivo {arquivo} não pôde ser lido: {e}')

# Verifica se alguma nota não foi encontrada e gera o log
notas_nao_encontradas = [nota for nota, encontrada in notas_encontradas.items() if not encontrada]

if notas_nao_encontradas:
    print("As seguintes notas fiscais não foram encontradas:", notas_nao_encontradas)
else:
    print("Todas as notas fiscais foram encontradas e movidas.")


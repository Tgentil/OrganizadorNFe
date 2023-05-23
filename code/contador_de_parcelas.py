"""
Este código Conta a quantidade de parcelas tem em um lote de NF-Es. Utilize esse script por último,
para evitar a contagem de parcelas de notas inutilizadas, canceladas e etc..
"""
import os
import xml.etree.ElementTree as ET
import sys

# Adicionando encoding para evitar erros de caracteres
sys.stdout.reconfigure(encoding='utf-8')

# Especifica o diretório onde estão os arquivos XML
DIRETORIO = "./data"

# Inicializa a contagem total de parcelas
TOTAL_PARCELAS = 0

# Loop pelos arquivos no diretório
for arquivo in os.listdir(DIRETORIO):
    if arquivo.endswith('.xml'):  # Verifica se é um arquivo XML
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(DIRETORIO, arquivo)

        try:
            # Lê o arquivo XML
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()

            # Conta a quantidade de tags <dup> no arquivo
            NUM_PARCELAS = len(root.findall(".//{http://www.portalfiscal.inf.br/nfe}dup"))

            if NUM_PARCELAS == 0:
                NUM_PARCELAS = 1

            TOTAL_PARCELAS += NUM_PARCELAS

        except IOError as e:
            print(f'O arquivo {arquivo} não pôde ser lido: {e}')
            continue  # Pula para o próximo arquivo

    # Debug
        # # Exibe o nome do arquivo e a quantidade de parcelas
        # print(f"Arquivo: {arquivo} - Parcelas: {NUM_PARCELAS}")

# Exibe o total de parcelas no lote de NF-e
print(f"Total de Parcelas: {TOTAL_PARCELAS}")

# Cria o relatório em arquivo de texto
RELATORIO= "relatorio_parcelas.txt"

with open(RELATORIO, "w", encoding='utf-8') as arquivo_relatorio:
    arquivo_relatorio.write(f"Total de Parcelas: {TOTAL_PARCELAS}\n")

print("Relatório gerado com sucesso.")

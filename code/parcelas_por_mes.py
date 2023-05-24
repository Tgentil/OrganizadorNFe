"""
Este script faz um relatório de quantas datas de vencimento de parecelas
tem em cada mês num lote dentro da pasta data.
"""
import os
import xml.etree.ElementTree as ET
from collections import defaultdict
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Especifica o diretório onde estão os arquivos XML
DIRETORIO = "./data"

# Dicionário para armazenar o contador de notas fiscais por mês
contador_meses = defaultdict(int)

# Loop pelos arquivos no diretório
for arquivo in os.listdir(DIRETORIO):
    if arquivo.endswith('.xml'):  # Verifica se é um arquivo XML
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(DIRETORIO, arquivo)

        try:
            # Lê o arquivo XML
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()

            # Obtém todas as tags <dVenc>
            tags_dvenc = root.findall(".//{http://www.portalfiscal.inf.br/nfe}dVenc")

            if tags_dvenc:
                # Verifica se há data de vencimento e extrai o mês
                for tag_dvenc in tags_dvenc:
                    data_vencimento = tag_dvenc.text
                    mes_vencimento = data_vencimento[5:7]  # Extrai o mês (formato YYYY-MM-DD)

                    # Incrementa o contador para o mês correspondente
                    contador_meses[mes_vencimento] += 1
            else:
                # Obtém a tag <dhEmi> para obter a data de emissão
                tag_dhemi = root.find(".//{http://www.portalfiscal.inf.br/nfe}dhEmi")

                if tag_dhemi is not None:
                    data_emissao = tag_dhemi.text
                    mes_emissao = data_emissao[5:7]  # Extrai o mês (formato YYYY-MM-DD)

                    # Incrementa o contador para o mês correspondente
                    contador_meses[mes_emissao] += 1

        except IOError as e:
            print(f'O arquivo {arquivo} não pôde ser lido: {e}')
            continue  # Pula para o próximo arquivo

# Cria o relatório em arquivo de texto
RELATORIO= "relatorio_parcelas.txt"

with open(RELATORIO, "w", encoding="utf-8") as arquivo_relatorio:
    arquivo_relatorio.write("Relatório de Data de Vencimento das Notas Fiscais\n")
    arquivo_relatorio.write("=============================================\n\n")

    TOTAL_PARCELAS = 0

    for mes, quantidade in contador_meses.items():
        arquivo_relatorio.write(f"Mês {mes}: {quantidade} notas fiscais\n")
        TOTAL_PARCELAS += quantidade

    arquivo_relatorio.write("\n")
    arquivo_relatorio.write("=============================================\n\n")
    arquivo_relatorio.write(f"Total de Parcelas: {TOTAL_PARCELAS} notas fiscais\n")

print("Relatório gerado com sucesso.")

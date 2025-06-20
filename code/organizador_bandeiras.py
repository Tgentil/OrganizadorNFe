""" Organizador de bandeiras de cartões de crédito e débito
"""
import os
import xml.etree.ElementTree as ET
import shutil
import sys

# Adicionando encoding para evitar erros de caracteres
sys.stdout.reconfigure(encoding='utf-8')

# Mapeamento de bandeiras
bandeiras = {
    '01': 'Visa',
    '02': 'Mastercard',
    '03': 'American Express',
    '07': 'Hipercard',
    '09': 'Cabal',
}

elo_codigos = ['05', '06']
outros_codigos = ['04', '08', '99']

mapeamento_bandeiras = {**bandeiras, **{codigo: 'Elo' for codigo in elo_codigos},
                        **{codigo: 'Outros' for codigo in outros_codigos}}

ROOT_FOLDER = "./out/cartoes"  # Pasta base

# Função para organizar os arquivos com base nas bandeiras
def organizar_por_bandeira(tipo_cartao):
    """
    Organiza arquivos XML de notas fiscais eletrônicas por bandeira de cartão de crédito.

    :param tipo_cartao: str com o nome da pasta que contém os arquivos XML a serem organizados.
    :return: None
    """
    diretorio = os.path.join(ROOT_FOLDER, tipo_cartao)  # Pasta de origem dos arquivos XML

    # Loop pelos arquivos no diretório
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.xml'):
            caminho_arquivo = os.path.join(diretorio, arquivo)

            try:
                tree = ET.parse(caminho_arquivo)
                myroot = tree.getroot()

                bandeira = obter_bandeira(myroot)
                destino = os.path.join(ROOT_FOLDER, tipo_cartao, bandeira)

                # Cria a pasta destino apenas se ela não existir
                if not os.path.exists(destino):
                    os.makedirs(destino)

                shutil.move(caminho_arquivo, os.path.join(destino, arquivo))

            except ET.ParseError as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")
            except AttributeError as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")
            except shutil.Error as e:
                print(f"Erro ao mover o arquivo {arquivo}: {e}")

    print(f"Arquivos na pasta {tipo_cartao} organizados!")

# Função para obter a bandeira do cartão do arquivo XML
def obter_bandeira(root):
    """
    Função que recebe um elemento XML root e retorna a bandeira correspondente à tag Tband.
    Caso a tag não esteja mapeada, retorna "Outros".

    Args:
        root (Element): Elemento XML root.

    Returns:
        str: Bandeira correspondente à tag Tband ou "Outros" caso não esteja mapeada.
    """
    tag_bandeira = root.find(".//{http://www.portalfiscal.inf.br/nfe}tBand")
    if tag_bandeira is not None and tag_bandeira.text in mapeamento_bandeiras:
        return mapeamento_bandeiras[tag_bandeira.text]
    return "Outros"

# Organiza os arquivos na pasta credito e depois em debito
organizar_por_bandeira("credito")
organizar_por_bandeira("debito")

print("Tarefa completa!")

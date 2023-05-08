"""
Este código é um organizador de arquivos XML. 
Ele lê arquivos XML em um diretório especificado e,
com base em informações dentro do arquivo, 
move o arquivo para um diretório correspondente. 
Os arquivos com a tag "cAut" 
em seu conteúdo são movidos para um diretório separado dos arquivos sem essa tag.
Além disso, os arquivos são movidos para diretórios diferentes dependendo do valor 
do elemento "tPag" no arquivo XML. 
Se o arquivo já existir no diretório de destino, uma mensagem de aviso será exibida.
Arquivos que não atendem aos critérios acima são movidos para um diretório
de arquivos cancelados e inutilizados. 
Quando a tarefa é concluída, uma mensagem de conclusão é exibida.

"""
import shutil
import os
import xml.etree.ElementTree as ET
import sys

# Adicionando encoding para evitar erros de caracteres
sys.stdout.reconfigure(encoding='utf-8')

# Define a pasta raiz
ROOT_FOLDER = "./out"

# Define uma lista de pastas a serem criadas
folders_to_create = [
    "dinheiro",
    "cartoes/credito",
    "cartoes/debito",
    "creditoLoja",
    "vales",
    "boletoBancario",
    "depositoBancario",
    "pix",
    "carteiraVirtual",
    "creditoVirtual",
    "outros",
    "diferentes"
]

# Loop sobre cada pasta a ser criada
for folder in folders_to_create:
    # Define o caminho completo da pasta
    folder_path = os.path.join(ROOT_FOLDER, folder)

    # Cria a pasta se ela não existir
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Exibe uma mensagem de conclusão quando a tarefa é finalizada
print("Pastas criadas com sucesso!")


class ArquivoNaoMovido(Exception):
    """cria uma exception caso não consiga mover o arquivo"""


# Especifica o diretório onde estão os arquivos XML
DIRETORIO = "./data"

# Loop pelos arquivos no diretório
for arquivo in os.listdir(DIRETORIO):
    if arquivo.endswith('.xml'):  # Verifica se é um arquivo XML
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(DIRETORIO, arquivo)

    # Loop pelos arquivos no diretório
PRIMEIRO_ARQUIVO = True
for arquivo in os.listdir(DIRETORIO):
    if arquivo.endswith('.xml'):  # Verifica se é um arquivo XML
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(DIRETORIO, arquivo)

        # verifica erro de leitura
        try:
            # Lê o arquivo XML
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()

            # Exibe mensagem informando que o primeiro arquivo foi lido com sucesso
            if PRIMEIRO_ARQUIVO:
                print("Primeiro arquivo lido com sucesso!")

        except IOError as e:
            print(f'O arquivo {arquivo} não pôde ser lido: {e}')
            continue  # Pula para o próximo arquivo

        # Lê o arquivo XML
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()

        # Verifica se a tag Caut existe no arquivo
        cAut = root.find(".//{http://www.portalfiscal.inf.br/nfe}cAut")
        if cAut is not None:
            # Constrói o nome do arquivo com a tag Caut
            nNF = root.find(".//{http://www.portalfiscal.inf.br/nfe}nNF")
            if nNF is not None:
                nome_arquivo = 'NFe' + nNF.text + '--' + cAut.text + '.xml'
            else:
                print(f"A tag nNF não foi encontrada no arquivo {arquivo}")
                PRIMEIRO_ARQUIVO = False
                continue  # Pula para o próximo arquivo
        else:
            # Constrói o nome do arquivo sem a tag Caut
            nNF = root.find(".//{http://www.portalfiscal.inf.br/nfe}nNF")
            if nNF is not None:
                nome_arquivo = 'NFe' + nNF.text + '.xml'
            else:
                print(f"A tag nNF não foi encontrada no arquivo {arquivo}")
                PRIMEIRO_ARQUIVO = False
                continue  # Pula para o próximo arquivo

        # Verifica o valor do elemento tPag
        tPag = root.find(".//{http://www.portalfiscal.inf.br/nfe}tPag").text
        if tPag == '01':
            DESTINO = "./out/dinheiro"
        elif tPag == '03':
            DESTINO = "./out/cartoes/credito"
        elif tPag == '04':
            DESTINO = "./out/cartoes/debito"
        elif tPag == '05':
            DESTINO = "./out/creditoLoja"
        elif tPag == '10' '11' '12' '13' :
            DESTINO = "./out/vales"
        elif tPag == '15':
            DESTINO = "./out/boletoBancario"
        elif tPag == '16':
            DESTINO = "./out/depositoBancario"
        elif tPag == '17':
            DESTINO = "./out/pix"
        elif tPag == '18':
            DESTINO = "./out/carteiraVirtual"
        elif tPag == '19':
            DESTINO = "./out/creditoVirtual"
        elif tPag == '99':
            DESTINO = "./out/outros"
        else:
            DESTINO = "./out/diferentes"

        # Verifica se o arquivo já existe no diretório de destino
        if os.path.exists(os.path.join(DESTINO, nome_arquivo)):
            print(
                f"O arquivo {nome_arquivo} já existe no diretório {DESTINO}.")
            # Move o arquivo para a pasta "repetidos" se já existe na pasta de destino
            REPETIDOS_DESTINO = "./out/repetidos"
            if os.path.exists(os.path.join(REPETIDOS_DESTINO, nome_arquivo)):
                print(
                    f"O arquivo {nome_arquivo} já existe na pasta de repetidos.")
            else:
                shutil.move(os.path.join(DESTINO, nome_arquivo),
                            os.path.join(REPETIDOS_DESTINO, nome_arquivo))
        else:
            try:
                # Move o arquivo para o destino correto
                shutil.move(caminho_arquivo, os.path.join(
                    DESTINO, nome_arquivo))
            except Exception as e:
                raise ArquivoNaoMovido(
                    f'O arquivo {nome_arquivo} não pôde ser movido: {e}') from e

        PRIMEIRO_ARQUIVO = False

# Move or arquivos que sobraram para pastas de inutilizadas e cancelamentos
DESTINO = "./out/SemTag"

# Loop pelos arquivos no diretório
for arquivo in os.listdir(DIRETORIO):
    if arquivo.endswith('.xml'):  # Verifica se é um arquivo XML
        # Obtém o caminho completo do arquivo
        caminho_arquivo = os.path.join(DIRETORIO, arquivo)

        # Move o arquivo para o diretório de destino
        try:
            shutil.move(caminho_arquivo, os.path.join(DESTINO, arquivo))
        except Exception as e:
            raise ArquivoNaoMovido(
                f'O arquivo {arquivo} não pôde ser movido: {e}') from e

# Caso houver arquivos repetidos mande os arquivos sem tag de volta para a pasta data
REPETIDOS_FOLDER = "./out/repetidos"
SEM_TAG_FOLDER = "./out/SemTag"
DATA_FOLDER = "./data"

if os.path.exists(REPETIDOS_FOLDER) and len(os.listdir(REPETIDOS_FOLDER)) > 0:
    for filename in os.listdir(SEM_TAG_FOLDER):
        file_path = os.path.join(SEM_TAG_FOLDER, filename)
        if os.path.isfile(file_path):
            shutil.move(file_path, DATA_FOLDER)
            continue  # continua o código

# Loop pelos diretórios dentro de "out"
for diretorio in os.listdir("./out"):
    caminho_diretorio = os.path.join("./out", diretorio)
    if os.path.isdir(caminho_diretorio) and not os.listdir(caminho_diretorio):
        # Remove o diretório vazio
        os.rmdir(caminho_diretorio)


# Cria um relatório txt dos arquivos em cada pasta
ROOT_FOLDER = "./out"

OUTPUT_FOLDER = "./out/relatorio"
output_file_path = os.path.join(OUTPUT_FOLDER, "contador.txt")

# Cria a pasta "relatorio" se ela ainda não existir
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Abre um arquivo de saída para gravar os resultados
with open(output_file_path, 'w', encoding='utf-8') as output_file:

    # Cria uma quebra de linha
    output_file.write("\n")

    # Loop sobre todas as pastas dentro da pasta raiz
    for folder_name in os.listdir(ROOT_FOLDER):
        folder_path = os.path.join(ROOT_FOLDER, folder_name)

        # Verifica se o caminho é uma pasta e se a pasta é diferente de "relatorio" e "cartoes"
        if os.path.isdir(folder_path) and folder_name != "relatorio" and folder_name != "cartoes":
            # Escreve o nome da pasta e o número de arquivos no arquivo de saída
            num_files = len(os.listdir(folder_path))
            output_file.write(f"{folder_name} - {num_files}\n")

# Define o caminho da pasta raiz
ROOT_FOLDER = "./out/cartoes"

OUTPUT_FOLDER = "./out/relatorio"
output_file_path = os.path.join(OUTPUT_FOLDER, "contadorV2.txt")

# Abre um arquivo de saída para gravar os resultados
with open(output_file_path, 'w', encoding='utf-8') as output_file:

    # Cria um titulo
    output_file.write("     Cartões:\n\n")

    # Loop sobre todas as pastas dentro da pasta raiz
    for folder_name in os.listdir(ROOT_FOLDER):
        folder_path = os.path.join(ROOT_FOLDER, folder_name)

        # Verifica se o caminho é uma pasta
        if os.path.isdir(folder_path):
            # Escreve o nome da pasta e o número de arquivos no arquivo de saída
            num_files = len(os.listdir(folder_path))
            output_file.write(f"{folder_name} - {num_files}\n")

# Define o caminho dos arquivos de saída
contador_path = os.path.join(OUTPUT_FOLDER, "contador.txt")
contadorV2_path = os.path.join(OUTPUT_FOLDER, "contadorV2.txt")
Relatorio_file_path = os.path.join(OUTPUT_FOLDER, "Relatorio.txt")

# Abre os arquivos de saída para leitura
with open(contador_path, 'r', encoding='utf-8') as contador_file, \
        open(contadorV2_path, 'r', encoding='utf-8') as contadorV2_file:

    # Lê o conteúdo dos arquivos de saída
    contador_content = contador_file.read()
    contadorV2_content = contadorV2_file.read()

# Abre o arquivo de saída para escrita
with open(Relatorio_file_path, 'w', encoding='utf-8') as Relatorio_file:

    # Escreve o conteúdo dos arquivos de saída no arquivo de saída combinado
    Relatorio_file.write(contadorV2_content)
    Relatorio_file.write(contador_content)

# Lê o conteúdo do arquivo
with open(Relatorio_file_path, 'r', encoding='utf-8') as Relatorio_file:
    relatorio_content = Relatorio_file.read()

    # Soma o número total de arquivos no relatório
    TOTAL_NUM_FILES = 0
    for line in relatorio_content.splitlines():
        if '-' in line:
            TOTAL_NUM_FILES += int(line.split('-')[1])

# Abre o arquivo de saída novamente para escrita e adiciona a soma total de arquivos
with open(Relatorio_file_path, 'a', encoding='utf-8') as Relatorio_file:
    Relatorio_file.write(
        f"\n------------------------\nTotal de arquivos - {TOTAL_NUM_FILES}\n")

# Remove os arquivos originais
os.remove(contador_path)
os.remove(contadorV2_path)

# Exibe uma mensagem de conclusão quando a tarefa é finalizada
print("Tarefa concluída!")

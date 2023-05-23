"""Script de organização de lotes de arquivos"""
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

# define o diretório onde os arquivos serão coletados
DIRETORIO = "./data"
if not os.path.exists(DIRETORIO):
    os.mkdir(DIRETORIO)

# percorre recursivamente todas as subpastas e move os arquivos para o diretório raiz
for root, dirs, files in os.walk(DIRETORIO):
    for file in files:
        src_path = os.path.join(root, file)
        dst_path = os.path.join(DIRETORIO, file)
        shutil.move(src_path, dst_path)

# lista todos os arquivos no diretório
arquivos = os.listdir(DIRETORIO)

# conta quantos arquivos existem no diretório
TOTAL_ARQUIVOS = 0
for arquivo in arquivos:
    if os.path.isfile(os.path.join(DIRETORIO, arquivo)):
        TOTAL_ARQUIVOS += 1

# escreve o total de arquivos em um arquivo txt
with open("TOTAL_ARQUIVOS.txt", "w", encoding="utf-8") as arquivo_txt:
    arquivo_txt.write(f"Total de arquivos: {TOTAL_ARQUIVOS}")


# define o tamanho do lote (quantos arquivos serão movidos por vez)
LOTE_SIZE = 1000

# define o contador/nome dos lotes
LOTE_COUNT = 1

# define o diretório onde os lotes serão movidos
lote_dir = f"./lotes/lote_{LOTE_COUNT}"

# cria a pasta onde o primeiro lote será movido (caso ainda não exista)
if not os.path.exists(lote_dir):
    os.makedirs(lote_dir)

# move cada arquivo para o diretório do lote correspondente
for i, arquivo in enumerate(arquivos):
    if os.path.isfile(os.path.join(DIRETORIO, arquivo)):
        if i % LOTE_SIZE == 0 and i != 0:
            # se atingir o tamanho do lote, cria uma nova pasta para o próximo lote
            LOTE_COUNT += 1
            lote_dir = f"./lotes/lote_{LOTE_COUNT}"
            os.makedirs(lote_dir)

        # move o arquivo para o diretório do lote correspondente
        shutil.move(os.path.join(DIRETORIO, arquivo), os.path.join(lote_dir, arquivo))

# apaga as pastas que sobraram em DIRETORIO
for item in os.listdir(DIRETORIO):
    item_path = os.path.join(DIRETORIO, item)
    if os.path.isdir(item_path):
        shutil.rmtree(item_path)

# move o arquivo de relatório para a pasta lotes
shutil.move("TOTAL_ARQUIVOS.txt", os.path.join(os.path.dirname(lote_dir), "TOTAL_ARQUIVOS.txt"))

# Exibe uma mensagem de conclusão quando a tarefa é finalizada
print("Tarefa concluída!")

import os

def alterar_xnome_dest(caminho_pasta, novo_nome_dest):
    arquivos = [arq for arq in os.listdir(caminho_pasta) if arq.endswith('.xml')]

    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        with open(caminho_completo, 'r', encoding='utf-8') as file:
            conteudo = file.read()

        # Localiza a tag <dest> e o campo <xNome>
        inicio_dest = conteudo.find('<dest>')
        if inicio_dest != -1:
            inicio_xnome_dest = conteudo.find('<xNome>', inicio_dest) + 7
            fim_xnome_dest = conteudo.find('</xNome>', inicio_xnome_dest)
            if inicio_xnome_dest != -1 and fim_xnome_dest != -1:
                conteudo = (
                    conteudo[:inicio_xnome_dest]
                    + novo_nome_dest
                    + conteudo[fim_xnome_dest:]
                )

        with open(caminho_completo, 'w', encoding='utf-8') as file:
            file.write(conteudo)

# Caminho para a pasta contendo os arquivos XML
caminho_pasta = './data'
# Novo nome para o campo <xNome> dentro de <dest>
novo_nome_dest = 'EMPRESA MODELO'

alterar_xnome_dest(caminho_pasta, novo_nome_dest)

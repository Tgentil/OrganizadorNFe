import os

def alterar_informacoes_em_nfce(caminho_pasta, cnpj_novo, novo_nome):
    arquivos = [arq for arq in os.listdir(caminho_pasta) if arq.endswith('.xml')]

    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        with open(caminho_completo, 'r', encoding='utf-8') as file:
            conteudo = file.read()

        # Localiza o emitente
        inicio_emitente = conteudo.find('<emit>')
        if inicio_emitente != -1:
            # Alterar CNPJ
            inicio_cnpj_emitente = conteudo.find('<CNPJ>', inicio_emitente)
            if inicio_cnpj_emitente != -1:
                inicio_cnpj_emitente += len('<CNPJ>')
                fim_cnpj_emitente = conteudo.find('</CNPJ>', inicio_cnpj_emitente)
                conteudo = conteudo[:inicio_cnpj_emitente] + cnpj_novo + conteudo[fim_cnpj_emitente:]
            
            # Alterar xFant, se existir
            index_xfant = conteudo.find('<xFant>', inicio_emitente)
            if index_xfant != -1:
                inicio_xfant = index_xfant + len('<xFant>')
                fim_xfant = conteudo.find('</xFant>', inicio_xfant)
                conteudo = conteudo[:inicio_xfant] + novo_nome + conteudo[fim_xfant:]
            
            # Alterar xNome
            inicio_xnome = conteudo.find('<xNome>', inicio_emitente)
            if inicio_xnome != -1:
                inicio_xnome += len('<xNome>')
                fim_xnome = conteudo.find('</xNome>', inicio_xnome)
                conteudo = conteudo[:inicio_xnome] + novo_nome + conteudo[fim_xnome:]
        
        with open(caminho_completo, 'w', encoding='utf-8') as file:
            file.write(conteudo)

# Caminho para a pasta contendo os arquivos XML das NFCe
caminho_pasta = './data'
# Novo CNPJ para substituir nos arquivos XML
cnpj_novo = '00000000000191'
# Novo nome fantasia e razão social
novo_nome = 'EMPRESA EXEMPLO LTDA ME'

alterar_informacoes_em_nfce(caminho_pasta, cnpj_novo, novo_nome)

import os

def modify_date_in_xml(file_path, new_year, new_month, output_directory):
    # Abrir o arquivo XML original
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Substituir o ano e o mês nas tags dhEmi, dhRecbto, dhSaiEnt e dVenc
    tags_to_modify = ['dhEmi', 'dhRecbto', 'dhSaiEnt', 'dVenc']
    for tag in tags_to_modify:
        start_pos = 0
        while True:
            start_tag = f'<{tag}>'
            end_tag = f'</{tag}>'
            start_idx = content.find(start_tag, start_pos)
            if start_idx == -1:
                break
            end_idx = content.find(end_tag, start_idx)

            # Extrair a data completa da tag
            date_full = content[start_idx + len(start_tag):end_idx]
            date_parts = date_full.split('T')
            date = date_parts[0].split('-')

            # Modificar ano e mês
            date[0] = str(new_year)  # Ano
            date[1] = f'{new_month:02}'  # Mês

            # Reconstruir a data
            new_date_full = '-'.join(date)
            if len(date_parts) > 1:
                new_date_full += 'T' + date_parts[1]  # Adicionar a parte do tempo, se houver

            # Substituir no conteúdo
            content = content[:start_idx + len(start_tag)] + new_date_full + content[end_idx:]
            start_pos = end_idx

    # Verificar se o diretório de saída existe, se não, criá-lo
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Gravar o arquivo XML modificado no diretório de saída
    base_filename = os.path.basename(file_path)
    modified_path = os.path.join(output_directory, base_filename.replace('.xml', '_modified.xml'))
    with open(modified_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Arquivo modificado salvo em: {modified_path}')

def process_all_xml_files(directory_path, new_year, new_month, output_directory):
    # Processar todos os arquivos XML na pasta especificada
    for filename in os.listdir(directory_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory_path, filename)
            modify_date_in_xml(file_path, new_year, new_month, output_directory)

# Caminho da pasta com os arquivos XML
directory_path = './data'
# Pasta de saída para os arquivos modificados
output_directory = './out'
# Ano e mês desejados
new_year = 2022
new_month = 5

# Chamar a função de modificação
process_all_xml_files(directory_path, new_year, new_month, output_directory)

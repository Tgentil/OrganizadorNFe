# Procura de Valor em Notas Fiscais

Este script procura por um valor específico na tag de pagamento (`<vPag>`) de um conjunto de notas fiscais. O objetivo é encontrar notas fiscais que possuam esse valor de pagamento.

## Pré-requisitos

Antes de utilizar o script, certifique-se de ter instalado o Python em seu sistema.

## Uso

Siga as instruções abaixo para utilizar o script:

1. Coloque todas as notas fiscais no diretório `data`. Certifique-se de que as notas fiscais estejam no formato XML.

2. Abra o arquivo `procura_valor.py` em um editor de texto.

3. No código-fonte, localize a variável `VALOR_PROCURADO` e substitua o valor `"100.00"` pelo valor que você deseja procurar nas notas fiscais.

4. Execute o script. O resultado será exibido no terminal.

    ```
    $ python nfe_finder.py
    ```

5. O script percorrerá todas as notas fiscais no diretório especificado e verificará se o valor de pagamento corresponde ao valor procurado. Caso seja encontrado, será exibida a mensagem informando em qual nota fiscal o valor foi encontrado.

6. Se nenhum valor correspondente for encontrado, uma mensagem indicando a ausência será exibida no terminal.

## Observações

- Certifique-se de que as notas fiscais estejam no formato XML

- Caso ocorra algum erro durante a leitura dos arquivos XML, uma mensagem de erro será exibida no terminal.

- O resultado da busca será exibido no terminal, indicando se o valor procurado foi encontrado ou não, e em qual nota fiscal ocorreu o correspondente.

- Certifique-se de que o diretório `data` contenha os arquivos XML das notas fiscais que você deseja pesquisar.

Certifique-se de ter as permissões necessárias para leitura e gravação nos diretórios e arquivos relevantes.

**Observação:** Caso seja necessário alterar o diretório onde estão os arquivos XML, você pode modificar a variável `DIRETORIO` no script para o caminho correto.

---
[**Voltar Para README Principal**](../../README.md)

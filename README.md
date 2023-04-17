# Organizador de arquivos XML

Este código é um organizador de arquivos XML que move os arquivos para diferentes diretórios com base em informações contidas nos arquivos XML.

## Funcionalidade

O código lê arquivos XML em um diretório especificado e, com base em informações dentro do arquivo, move o arquivo para um diretório correspondente. Os arquivos com a tag cAut em seu conteúdo são movidos para um diretório separado dos arquivos sem essa tag. Além disso, os arquivos são movidos para diretórios diferentes dependendo do valor do elemento tPag no arquivo XML. Se o arquivo já existir no diretório de destino, uma mensagem de aviso será exibida. Arquivos que não atendem aos critérios acima são movidos para um diretório de arquivos cancelados e inutilizados. Quando a tarefa é concluída, uma mensagem de conclusão é exibida.

## Instalação

Este código não requer nenhuma biblioteca adicional, além das bibliotecas padrão do Python. Basta clonar o repositório ou copiar o código para o seu ambiente.

## Estruturação do código

```
+--./
|-- organizador_nfce.py
|-- path.py
|-- README
|  +--.vscode/
|   |-- settings.json
|  +--backup/
|   |  +--out/
|   |   |  +--cartoes/
|   |   |   |  +--credito/
|   |   |   |  +--debito/
|   |   |  +--diferentes/
|   |   |  +--dinheiro/
|   |   |  +--outros/
|   |   |  +--relatorio/
|   |   |  +--repetidos/
|   |   |  +--semTag/
|  +--data/
|  +--out/
|   |  +--cartoes/
|   |   |  +--credito/
|   |   |   |-- NFe789822.xml
|   |   |  +--debito/
|   |   |   |-- NFe789825.xml
|   |   |   |-- NFe789831.xml
|   |  +--diferentes/
|   |   |-- NFe789834.xml
|   |  +--dinheiro/
|   |   |-- NFe789821.xml
|   |  +--outros/
|   |   |-- NFe789833.xml
|   |  +--relatorio/
|   |   |-- Relatorio.txt
|   |  +--repetidos/
|   |   |-- NFe789831.xml
|   |  +--semTag/
```

## Como utilizar o código

Para utilizar este código, é necessário colocar os arquivos XML que deseja organizar dentro da pasta `data`. Em seguida, execute o código e os arquivos serão organizados e armazenados na pasta `out`. Um relatório em formato TXT será gerado, mostrando quantos arquivos foram movidos para cada pasta.

Após o uso do código, é recomendável mover a pasta `out` para o local desejado. Para reutilizar o código em outra ocasião, basta copiar a pasta `out` da pasta `backup` dentro da pasta principal. Dessa forma, os arquivos já organizados serão preservados e você poderá continuar trabalhando com a organização dos arquivos XML.

## Uso

Para executar o código, basta executar o arquivo Python `organizador_nfce.py`. O código será executado e organizará todos os arquivos XML no diretório especificado. O código exibirá uma mensagem de aviso se o arquivo já existir no diretório de destino e uma mensagem de conclusão após a organização dos arquivos.

## Arquivos repetidos

Caso houver arquivos repetidos, o código irá identificá-los e salvá-los dentro da pasta `repetidos` dentro da pasta `out`. Além disso, o relatório gerado também irá informar quantos arquivos foram identificados como repetidos.

Para continuar a utilização do código, é importante salvar o relatório gerado e deletar os arquivos em `data` que foram processados pelo código. Em seguida, é preciso importar os arquivos de repetidos para a pasta `data` e rodar o código novamente.

## Exemplo de saída Relatório

```
     Cartões:

credito - 5073
debito - 6841

diferentes - 2
dinheiro - 4175
outros - 1663
repetidos - 0
semTag - 0

------------------------
Total de arquivos - 17754
```

## Exceptions

Se o arquivo não puder ser lido, o código irá pular para o próximo arquivo. Se não for possível mover o arquivo, será lançada uma exceção ArquivoNaoMovido.

## Autor

* Thiago Da Silveira Gentil
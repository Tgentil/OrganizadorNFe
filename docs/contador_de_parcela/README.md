# Contador de Parcelas de NF-E

Este script em Python é usado para contar a quantidade de parcelas em um lote de NF-Es. É importante executar este script por último, para evitar a contagem de parcelas de notas inutilizadas, canceladas e outras situações.


## Como utilizar

1. Coloque os arquivos XML contendo as NF-Es no diretório `data`.

2. Abra um terminal ou prompt de comando e navegue até o diretório onde o script está salvo.

3. Execute o script com o seguinte comando:
```
python contador_parcelas.py
```

4. Aguarde até que a execução seja concluída.

5. Após a execução, o script exibirá o total de parcelas encontrado no lote de NF-Es.

6. Além disso, será gerado um arquivo de relatório chamado `relatorio_parcelas.txt` no mesmo diretório do script, contendo o total de parcelas.

Certifique-se de ter as permissões necessárias para leitura e gravação nos diretórios e arquivos relevantes.

**Observação:** Caso seja necessário alterar o diretório onde estão os arquivos XML, você pode modificar a variável `DIRETORIO` no script para o caminho correto.



---
[**Voltar Para README Principal**](../../README.md)

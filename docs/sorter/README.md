# Organização de Lotes de Arquivos

Este script em Python é usado para organizar lotes de arquivos em uma pasta. Ele move os arquivos do diretório atual e suas subpastas para um diretório raiz específico, divide-os em lotes menores e os move para pastas separadas.


## Como utilizar

1. Coloque os arquivos que deseja organizar dentro da pasta `data`. Você pode ter subpastas dentro dela, pois o script percorrerá recursivamente todas as subpastas.

2. Abra um terminal ou prompt de comando e navegue até o diretório onde o script está salvo.

3. Execute o script com o seguinte comando:
```
python organizacao_lotes_arquivos.py
```

4. Aguarde até que a execução seja concluída.

5. Após a execução, você encontrará os seguintes resultados:

- Os arquivos e subpastas que estavam dentro da pasta `data` terão sido movidos para o diretório raiz.
- Os arquivos serão divididos em lotes menores, definidos pelo tamanho especificado na variável `LOTE_SIZE` (atualmente definida como 1000).
- Cada lote terá uma pasta correspondente na pasta `lotes`. Por exemplo, o primeiro lote será movido para a pasta `lote_1`, o segundo lote para a pasta `lote_2` e assim por diante.
- O script também criará um arquivo chamado `TOTAL_ARQUIVOS.txt` que conterá o total de arquivos movidos.

Certifique-se de ter as permissões necessárias para leitura, gravação e exclusão nos diretórios e arquivos relevantes.

**Observação:** Certifique-se de entender o código antes de executá-lo para evitar problemas indesejados. Você pode ajustar o tamanho do lote modificando a variável `LOTE_SIZE` no script.

---
[**Voltar Para README Principal**](../../README.md)

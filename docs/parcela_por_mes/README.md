# Relatório de Vencimentos das Notas Fiscais

Este script em Python é usado para gerar um relatório que conta quantas datas de vencimento de parcelas existem em cada mês de um lote de NF-Es. O lote de NF-Es deve estar localizado na pasta "data".


## Como utilizar

1. Coloque os arquivos XML contendo as NF-Es no diretório `data`.

2. Abra um terminal ou prompt de comando e navegue até o diretório onde o script está salvo.

3. Execute o script com o seguinte comando:
```
python relatorio_vencimentos.py
```

4. Aguarde até que a execução seja concluída.

5. Após a execução, o script gerará um arquivo de relatório chamado `relatorio_vencimentos.txt` no mesmo diretório do script.

6. Abra o arquivo de relatório para ver o resultado. Ele conterá informações sobre a quantidade de notas fiscais por mês, com base nas datas de vencimento das parcelas.

Certifique-se de ter as permissões necessárias para leitura e gravação nos diretórios e arquivos relevantes.

**Observação:** Caso seja necessário alterar o diretório onde estão os arquivos XML, você pode modificar a variável `DIRETORIO` no script para o caminho correto.

Em caso da nota não ter data de vencimento ( normalmente notas sem duplicatas )  ele vai contabilizar o mês de emissão como o de pagamento.

---
[**Voltar Para README Principal**](../../README.md)

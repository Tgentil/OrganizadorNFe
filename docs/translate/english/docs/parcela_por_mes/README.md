# Invoice Dates Report

This Python script is used to generate a report that counts how many due dates for installments exist in each month for a batch of invoices. The batch of invoices should be located in the "data" folder.


## How to Use

1. Place the XML files containing the invoices in the `data` directory.

2. Open a terminal or command prompt and navigate to the directory where the script is saved.

3. Run the script with the following command:
```
python parcela_por_mes.py
```

4. Wait for the execution to complete.

5. After execution, the script will generate a report file called `relatorio_parcelas.txt` in the same directory as the script.

6. Open the report file to see the result. It will contain information about the number of invoices per month based on the due dates of the installments.

Make sure you have the necessary permissions for reading and writing in the relevant directories and files.

**Note:** If you need to change the directory where the XML files are located, you can modify the `DIRECTORY` variable in the script to the correct path.

In case the invoice does not have a due date (usually invoices without installments), it will count the month of issuance as the payment month.

---
[**Back to Main README**](../../README.md)
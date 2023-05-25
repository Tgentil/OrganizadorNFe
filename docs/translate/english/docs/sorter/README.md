# File Batches Organization

This Python script is used to organize batches of files in a folder. It moves the files from the current directory and its subdirectories to a specific root directory, divides them into smaller batches, and moves them to separate folders.

## How to Use

1. Place the files you want to organize inside the `data` folder. You can have subfolders within it, as the script will recursively traverse all subfolders.

2. Open a terminal or command prompt and navigate to the directory where the script is saved.

3. Run the script with the following command:

```
python organizacao_lotes_arquivos.py
```

4. Wait for the execution to complete.

5. After execution, you will find the following results:

-   The files and subfolders that were inside the `data` folder will have been moved to the root directory.
-   The files will be divided into smaller batches, defined by the size specified in the `LOTE_SIZE` variable (currently set to 1000).
-   Each batch will have a corresponding folder in the `lotes` folder. For example, the first batch will be moved to the `lote_1` folder, the second batch to the `lote_2` folder, and so on.
-   The script will also create a file called `TOTAL_ARQUIVOS.txt` that will contain the total number of moved files.

Make sure you have the necessary permissions for reading, writing, and deleting in the relevant directories and files.

**Note:** Make sure you understand the code before running it to avoid unwanted issues. You can adjust the batch size by modifying the `LOTE_SIZE` variable in the script.

---

[**Back to Main README**](../../README.md)

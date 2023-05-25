# Invoice Value Search

This script searches for a specific value in the payment tag (`<vPag>`) of a set of invoices. The goal is to find invoices that have this payment value.

## Prerequisites

Before using the script, make sure you have Python installed on your system.

## Usage

Follow the instructions below to use the script:

1. Place all the invoices in the `data` directory. Make sure the invoices are in XML format.

2. Open the `search_value.py` file in a text editor.

3. In the source code, locate the `SEARCH_VALUE` variable and replace the value `"100.00"` with the value you want to search for in the invoices.

4. Run the script. The result will be displayed in the terminal.

    ```
    $ python invoice_finder.py
    ```

5. The script will iterate through all the invoices in the specified directory and check if the payment value matches the searched value. If a match is found, a message will be displayed indicating which invoice the value was found in.

6. If no matching value is found, a message indicating the absence will be displayed in the terminal.

## Notes

- Make sure the invoices are in XML format.

- If an error occurs while reading the XML files, an error message will be displayed in the terminal.

- The search result will be displayed in the terminal, indicating whether the searched value was found or not, and in which invoice it occurred.

- Make sure the `data` directory contains the XML files of the invoices you want to search.

Ensure you have the necessary permissions for reading and writing in the relevant directories and files.

**Note:** If you need to change the directory where the XML files are located, you can modify the `DIRECTORY` variable in the script to the correct path.

---
[**Back to Main README**](../../README.md)
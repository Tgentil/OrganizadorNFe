# NF-E Organizer

[![Translate](https://img.shields.io/badge/Translate-Portugu%C3%AAs%20%F0%9F%87%A7%F0%9F%87%B7-blue.svg)](../../../README.md)

This code is an XML file organizer that moves the files to different directories based on the information contained within the XML files.

## Functionality

The code reads NF-Es (Nota Fiscal Eletrônica) in XML files within the `data` directory, and based on the information within the file, moves the file to a corresponding directory. The files are moved to different directories depending on the value of the `tPag` element in the XML file. If the file already exists in the destination directory, a warning message is displayed. Files that do not meet the above criteria are moved to a canceled and unused files directory. When the task is completed, a completion message is displayed.

## Installation

This code does not require any additional libraries, other than the standard Python libraries. Simply clone the repository or copy the code to your environment.

## Code Structure

```
+--./
|-- README.md
|  +--.github/
|   |  +--workflows/
|   |   |-- pylint.yml
|  +--.vscode/
|   |-- settings.json
|  +--code/
|   |-- parcel_counter.py
|   |-- nfce_organizer.py
|   |-- parcels_per_month.py
|   |-- sorter.py
|  +--data/
|   |-- .gitkeep
|  +--docs/
|   |  +--parcel_counter/
|   |   |-- README.md
|   |  +--parcels_per_month/
|   |   |-- README.md
|   |  +--sorter/
|   |   |-- README.md
```

## How to Use the Code

To use this code, you need to place the XML files you want to organize inside the `data` folder. Then, run the code and the files will be organized and stored in the `out` folder. A TXT report will be generated, showing how many files were moved to each folder.

After using the code, it is recommended to move the `out` folder to the desired location if you want to reuse the code in the future. This way, the already organized files will be preserved, and you can continue working with the organization of XML files.

## Usage

To execute the code, simply run the `nfce_organizer.py` Python file. The code will run and organize all the XML files in the specified directory. The code will display a warning message if the file already exists in the destination directory and a completion message after organizing the files.

## Duplicate Files

If there are duplicate files, the code will identify them and save them within the `duplicates` folder inside the `out` folder. Additionally, the generated report will also indicate how many files were identified as duplicates.

To continue using the code, it is important to save the generated report, delete the processed files in the `data` folder, import the duplicate files back into the `data` folder, and run the code again.

## Example Output - Report

```
     Cards:

credit - 5073
debit - 6841

different - 2
cash - 4175
others - 1663
duplicates - 0
untagged - 0

------------------------
Total files - 17754
```

## Example Output - Parcel Report

```

Invoice Due Date Report
=============================================

Month 02: 281 invoices
Month 03: 221 invoices
Month 04: 3 invoices

=============================================

Total Parcels: 505 invoices

```

## Exceptions

If a file cannot be read, the code will skip to the next file. If it is not possible to move the file, a `FileNotMoved` exception will

be raised.

# Other Scripts

1. [README - NF-e Finder by value](./docs/nfe_finder/README.md)
2. [README - Parcels per Month](./docs/parcelas_por_mes/README.md)
3. [README - Sorter](./docs/sorter/README.md)

**Note:** Before using any of the scripts, make sure you have Python installed on your machine.

## Author

-   Thiago Da Silveira Gentil

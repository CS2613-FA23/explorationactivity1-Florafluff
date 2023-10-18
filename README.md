### 1. Which package/library does the sample program demonstrate?
- The sample program demonstrates the python library [pandas](https://pandas.pydata.org/docs/).

### 2. How does someone run your program?
- To run the program input ``pip install pandas in the terminal, then just do ``python SpreadsheetEditor.py`` in the terminal in the same directory the file is in.
- Then enter the file name of your ``.csv`` spreadsheet when prompted.
- if you get an ``ModuleNotFoundError: No module named 'openpyxl'`` error when exporting to Excel then run the command ``pip install openpyx1``

### 3. What purpose does your program serve?
- The program allows you to edit a ``.csv`` spreadsheet.
- You can add and remove columns and rows, changing the data inside them as you do.
- The program allows you to output your spreadsheet as a ``.csv`` (command seperated values) or a ``.xlsx`` (Excel document).

### 4. What would be some sample input/output?
- Any ``.csv`` file with at least 2 lines in it with the first line being the column names is a valid input.
- the file ``ExampleSpreadsheet.csv`` is an example of a valid input.
- Some other valid inputs would be: 

![Spreadsheet with numeric column names with all their data being 0s](https://cdn.discordapp.com/attachments/319987558509576201/1161821018470490182/8c44DUo5Rg6Kre35BMNkNg.png?ex=6539b124&is=65273c24&hm=b07990277c0c1a4a6f8c2b3329c24edcb928e1d216bf0416258a583603db9c1e&)

![Spreadsheet with alphabetic column names and mixed data types](https://cdn.discordapp.com/attachments/319987558509576201/1161821959672320050/image.png?ex=6539b204&is=65273d04&hm=470227a183835ab402354c20b374ecc6b4360e909c1651b7c33d1ad66a0ce132&)

![Spreadsheet with alphabet and numeric column names and numeric data](https://cdn.discordapp.com/attachments/319987558509576201/1161822885774635028/image.png?ex=6539b2e1&is=65273de1&hm=45cfbd8690eb9706c6d2f6d890b085feed82364d9d51ac1511dab9a9206a2385&)
- An Excel output for ``ExampleSpreadsheet.csv`` where the a column named ``column8`` was added:

![Edited ExampleSpreadsheet.csv in Excel](https://cdn.discordapp.com/attachments/319987558509576201/1161826179762896957/image.png?ex=6539b5f2&is=652740f2&hm=e49868418ae8d3a6838b47c171d70255c8846c6d5e8d09c7511a95d7000867cf&)

- A ``.csv`` output for ``ExampleSpreadsheet.csv`` where the a column named ``column8`` was added:

![Edited ExampleSpreadsheet.csv outputed as a .csv file](https://cdn.discordapp.com/attachments/319987558509576201/1161853051657789480/image.png?ex=6539cef9&is=652759f9&hm=c07dab3c57cfd3bae04268aaf099cc72feb60a6b6723727cf49cb1c91d87eff6&)

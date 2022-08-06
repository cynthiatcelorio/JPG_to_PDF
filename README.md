# JPG to PDF converter

Python script to convert a folder of images to combine all of then in a single file.

You can use it to combine the images of your class notes, your manga volumes or whatever you want.

## How does it works?

To explain this, I will use as an example a manhwa chapter that I have in images:

### 1. Clone the repository on your computer

### 2. Install required modules

```
pip install fpdf 
```
### 3. Locate the folder in which the images to be converted to pdf are located and copy the path (It is important that this folder only contains images) 

![Captura de pantalla (1285)](https://user-images.githubusercontent.com/16228113/183226601-4eb7414d-d377-46d4-b1ab-36371aed3c59.png)

The files will be sorted alphabetically in the pdf.
If you see, images 2 and 3 have a different format. This program is intended for numbers less than 10 to be written in the following format 01, 02, ... not 1, 2, 3... because function sort does not order it correctly. When running the program the file names will be corrected so that this is not a problem.
I have coded it for my type of filename, you can edit it as you wish.

### 4. Run the program with your favorite IDE

### 5. Enter the path, previously copied, of the images to be converted

### 6. Enter the name of the pdf

It is important that the name ends with ".pdf"

![Captura de pantalla (1286)](https://user-images.githubusercontent.com/16228113/183226613-48412aa4-f991-48b3-bf2b-d611e1fcbfad.png)

After entering the path and the name of the document to be generated, we will have our pdf ready! It will be located in the path in which we have the code.

![Captura de pantalla (1284)](https://user-images.githubusercontent.com/16228113/183226681-b641636a-7193-4140-89b2-d0b8acb3150b.png)

We can see how the format of the files has been changed as mentioned above.



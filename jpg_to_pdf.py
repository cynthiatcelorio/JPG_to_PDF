import os
from fpdf import FPDF

pdf = FPDF()
imagelist = []                                                

# Function that rename file from format string_X to string_0X because list.sort orders the numbers this way:  1, 11, 12, 2, 21... 
# We need to put a zero to sort it correctly: 01, 02, 03 .., 11, 12..

def rename_file(full_path, filename):
    if filename[-6] == '_':
        newname = full_path.replace(f"_{filename[-5]}.", f"_0{filename[-5]}.") 
        os.rename(full_path, newname)

        return newname
    else:
        return full_path                                # If the number is not to be changed, it is returned as before
        

# Function to add images to a list 

def add_files(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:

           full_path = os.path.join(dirpath, filename)              
           image_name = rename_file(full_path, filename)            # Rename the file if required
           imagelist.append(image_name)

    imagelist.sort()                                                # Sort the images by name

    print("\nFound " + str(len(imagelist)) + " image files. Converting to PDF....\n")


def create_pdf(name):
    for image in imagelist:
        pdf.add_page()
        pdf.image(image, 0, 0, 210, 297)                           # Dimensions of an A4 size sheet.

    pdf.output(name, "F")                                 # Save the PDF.

    print("PDF generated successfully!")



# inputs

folder = input("Enter the path to the folder of images you want to convert to pdf: ")                 # Folder containing all the images
name = input("Enter the name of the document to create (_name.pdf): ")                                # Name of the PDF file to generate


add_files(folder)
create_pdf(name)

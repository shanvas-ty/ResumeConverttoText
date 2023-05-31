# Resume Conversion-Main program
#################################

This program is designed to convert files in PDF, DOC, and DOCX formats to text file format.
 It provides a simple command-line interface for converting files located in a specific directory.

## Prerequisites

Make sure you have the following dependencies installed:

- CVconversion_word_to_txt
- CVconversion_pdf_to_txt
- os
- re

## Usage

1. Place the files you want to convert in the "./ResumeConversion/InputDataLoad" directory.
2. Run the program by executing the following command:

3. The program will list the folders/files present in the specified directory.
4. If there are no files available for conversion, a message will be displayed indicating the same.
5. If there are files available, the program will iterate over each file in the directory.
6. Files with a .docx or .doc extension will be converted to text format using the `CVconversion_word_to_txt.word_to_txt()` function.
7. Files with a .pdf extension will be converted to text format using the `CVconversion_pdf_to_txt.pdf_to_txt()` function.
8. The converted text files will be saved in the same directory with the original file name and a .txt extension.
9. The program will display a message indicating the completion of the conversion process.

## Exit

To exit the program, enter '1' when prompted.

###################################################################################
# PDF to Text Conversion
########################

This program converts PDF files into text format using Optical Character Recognition
 (OCR) with the help of Tesseract OCR and other Python libraries.

## Prerequisites

Before running the program, make sure you have completed the following steps:

1. Download and install Tesseract OCR by following the instructions provided in the `tesseract-ocr-w64-setup-5.3.1.20230401` installer.
2. Install the required Python packages by running the following commands:
   pip install pytesseract
   pip install pdf2image

## Usage

1. Place the PDF file you want to convert in the same directory as the script.

2. The program will convert each page of the PDF into an image using the `convert_from_path` function from the `pdf2image` library.
3. For each image, OCR is performed using the Tesseract OCR engine through the `pytesseract.image_to_string` function to extract the text.
4. The extracted text is saved in a text file named "convert_pdf2text3.txt" in the "./OutputData/" directory.
5. Once the conversion is complete, the program will display the file path where the converted text file is saved.

## Output

The program generates a text file containing the extracted text from the PDF file. The file is saved as "convert_pdf2text3.txt" in the "./OutputData/" directory.

## Note

Please note that the accuracy of the OCR process depends on the quality and clarity of the PDF file. Additionally, make sure the Tesseract OCR installation is configured properly for the desired language.
###########################################################################################

# Word to Text Conversion 
##########################

This program converts Word documents into text format using the `docx2txt` library.

## Usage

1. Place the Word document you want to convert in the same directory as the script.
2. The program will extract the text content from the Word document using the `docx2txt.process` function.
3. The extracted text is saved in a text file named "convert_word2text.txt" in the "./OutputData/" directory.
4. Once the conversion is complete, the program will display the file path where the converted text file is saved.

## Output

The program generates a text file containing the extracted text from the Word document. The file is saved as "convert_word2text.txt" in the "./OutputData/" directory.

## Note

Please note that the accuracy of the conversion process depends on the formatting and complexity of the Word document. Additionally, the program assumes the Word document is in the `.docx` format.









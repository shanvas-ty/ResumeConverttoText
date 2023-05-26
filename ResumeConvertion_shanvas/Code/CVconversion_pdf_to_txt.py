# download  tesseract-ocr-w64-setup-5.3.1.20230401 and install
# pip install pytesseract
#pip install pdf2image

#<..>   imports the necessary modules: os, pytesseract, Image from PIL (Python Imaging Library), and convert_from_path from pdf2image.
import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

#<..>   function pdf_to_txt(newfilepath) is defined, which takes the path of the PDF file as an argument.
def pdf_to_txt(newfilepath): 

    #<..> convert_from_path function is called with the newfilepath argument to convert the PDF pages into images.
    #       The 500 parameter specifies the DPI (dots per inch) value for the images.
    pages = convert_from_path(newfilepath,500)
    # print(pages)

    #<..> A loop iterates over each page/image obtained from the PDF conversion.
    for i,img in enumerate(pages):
        # print(img)

        #<..> Inside the loop, OCR is performed using pytesseract.image_to_string() to extract text from the current image.The lang='eng' parameter specifies that English is the language being used for OCR.
        text = pytesseract.image_to_string(img,lang='eng')

        #<..> The extracted text is written to a text file named "convert_pdf2text3.txt" using the open() function in write mode ("w"). The file is saved in the "./OutputData/" directory.
        file1=open("./OutputData/convert_pdf2text3.txt","w") # open the file in append & read mode
        file1.write(text)     
    print("........Sucessfully converted your pdf file into text format.....") 
    filepath=os.getcwd()  #<..> file path of the converted PDF text file is printed using os.getcwd() to get the current working directory 
    print("Converted pdf saved file path: ",os.path.join(filepath,"OutputData\convert_pdf2text3.txt"))  #<..> combine the directory path with the filename


# path = "./OutputData/convert_pdf2text3.txt"
# pdf_to_txt(path)

















#####################################
#     # install>    pip install PyPDF2

#         # importing required modules
# from PyPDF2 import PdfReader
# import os
# def pdf_to_txt(newfilepath):
#     # print("Filepath of pdftotxt program=",newfilepath)
#     # creating a pdf reader object
#     # os.chdir("./InputDataLoad")     #it change directory
#     # reader = PdfReader("./InputDataLoad/sample_pdfcv2.pdf","rb") # we need to open the file. So we use the function open to open the file for reading in binary mode.
#     reader = PdfReader(newfilepath,"rb") # we need to open the file. So we use the function open to open the file for reading in binary mode.
#     # os.chdir("../")
#     # print("path in pdf:",os.getcwd())   
#     # number of pages in pdf file
#     n = len(reader.pages)
#     # os.chdir("./OutputData")
#     for i in range(0,n):

#         # getting a specific page from the pdf file
#         page = reader.pages[i]

#         # extracting text from page
#         text  = page.extract_text()
#         # print(text)

#         # save to a text file for later use
#         # copy the path where the script and pdf is placed
#         file1=open("./OutputData/convert_pdf2text1.txt","a+") # open the file in append & read mode
#         file1.writelines(text)

#         # file1.seek(0) #Place the file pointer at the beginning of the file
#         # print(file1.read()) #Read text from the file
    
#         # closing the text file object
#         file1.close()

#     # os.chdir("../")     
#     # print(os.getcwd())  #it go back to the previous directory
#     # M=['*.txt']
#     # L=(os.listdir()) 
#     # print(L)
#     # for i in L:
#     #     if i in M:
#     #         print(i)
#     ###############################OR###############################
#                     #    OR
#     # https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
#     # https://www.scaler.com/topics/extract-text-from-pdf-python/
#     # https://pypi.org/project/text-extractor/
#     # pip install text_extractor
# from text_extractor import text_extraction    
# def pdf_to_txt(newfilepath):
#     # filepath = "./InputDataLoad/sample_pdfcv2.pdf"
#     filepath = newfilepath
#     output_text = text_extraction(filepath)

#     # print(output_text)
#     file1=open("./OutputData/convert_pdf2text2.txt","a+") # open the file in append & read mode
#     file1.writelines(output_text)
#     file1.close()
# # pdf_to_txt()    
# ###############################################################################
#                      #OR
# # download  tesseract-ocr-w64-setup-5.3.1.20230401 and install
# # pip install pytesseract
# #pip install pdf2image
# import pytesseract
# from PIL import Image
# from pdf2image import convert_from_path
# def pdf_to_txt(newfilepath):
#     # pdf_path = newfilepath
#     # pdf_path = "./InputDataLoad/sample_wordcv.docx"
#     pages = convert_from_path(newfilepath,500)
#     # print(pages)
#     for i,img in enumerate(pages):
#         # print(img)
#         text = pytesseract.image_to_string(img,lang='eng')
#         file1=open("./OutputData/convert_pdf2text3.txt","w") # open the file in append & read mode
#         file1.write(text)     
#     # os.path.join(filepath,filename)    
     
#     # print("Converted pdf file saved location =",os.chdir(""./OutputData/convert_pdf2text3.txt))        
#     print("........Sucessfully converted your pdf file into text format.....") 
#     filepath=os.getcwd()
#     print("Converted pdf saved file path: ",os.path.join(filepath,"OutputData\convert_pdf2text3.txt"))  

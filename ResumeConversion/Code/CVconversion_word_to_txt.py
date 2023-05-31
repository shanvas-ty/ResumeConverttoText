# https://djangocentral.com/convert-a-docx-file-to-text-file/
# pip install docx2txt

#<..> imports the necessary modules: docx2txt for converting Word documents to text and os for interacting with the operating system.
import docx2txt 
import os

#<..>  word_to_txt(newfilepath) function is defined, which takes the path of the Word document as an argument.
def word_to_txt(newfilepath):
    # print("Filepath of wordtotxt program=",newfilepath)

    #<..> docx2txt.process() function is called with newfilepath as an argument
    #                      to extract the text content from the Word document. The extracted text is stored in the text variable
    text = docx2txt.process(newfilepath)

    #<..> A text file named "convert_word2text.txt" is opened in write mode ("w") using the open() function and assigned to file1. This file will store the extracted text
    file1=open("./OutputData/convert_word2text.txt","w") # open the file in append & read mode

    #<..>The extracted text is written to the opened file using file1.writelines(text)
    file1.writelines(text)

    # closing the text file object
    file1.close()    

    print("........Sucessfully converted your word file into text format.....") 

    #<..> current working directory is obtained using os.getcwd() and assigned to filepath.
    filepath=os.getcwd() 
    
    #<..> file path of the converted Word text file is printed by combining filepath with the filename using os.path.join(). 
    #      It will be in the "./OutputData/convert_word2text.txt" format.
    print("Converted word saved file path: ",os.path.join(filepath,"OutputData\convert_word2text.txt"))  

# path = "./InputDataLoad/sample_wordcv.docx"
# word_to_txt(path)
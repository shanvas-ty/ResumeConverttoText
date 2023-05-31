#<..>  importing the necessary modules (CVconversion_word_to_txt, CVconversion_pdf_to_txt, os, and re).
import CVconversion_word_to_txt    
import CVconversion_pdf_to_txt     
import os
import re

#<..> The main() function is defined, which is responsible for converting the files in the specified
#             directory to text format.

def main():
    #<..> changes the current working directory to the 
    #                     ./ResumeConvertion_shanvas/InputDataLoad folder using os.chdir().
    os.chdir("./ResumeConvertion_shanvas/InputDataLoad")
    filepath = os.getcwd()
    # print("newfilepath in main program=",filepath)

    #<..> list of folders/files in the current directory is obtained using os.listdir() and stored in the folder variable.
    folder = os.listdir()
    print("Folders inside filepath =",folder)

    os.chdir("../")
    # filepath2 = os.getcwd()
    # print("file path after change diretory:",filepath2)
    
    #<..> If the folder list is empty, a message is printed indicating that no files are available for conversion.
    if folder ==[]: 
        print("Please..Upload your file in the directory for conversion to text")
    else:    
        #<..> If the folder list is not empty, the script iterates over each file in the directory.
        for filename in folder:

            #<..>If a file with a .docx or .doc extension is found, the CVconversion_word_to_txt.word_to_txt()
            #     function is called with the file path as an argument to convert the Word document to a text file.
            if(re.search('.(docx|doc)$',filename)):
                # print("os path",os.path)
                newfilepath=os.path.join(filepath,filename) # here append filename with current filepath 
                CVconversion_word_to_txt.word_to_txt(newfilepath)  #call function for convert word2text
                # print(filename)

            #<..> If a file with a .pdf extension is found, the CVconversion_pdf_to_txt.pdf_to_txt()
            #     function is called with the file path as an argument to convert the PDF to a text file.    
            elif(re.search('.(pdf)$',filename)):
                # print("file in pdf program",filename)
                newfilepath=os.path.join(filepath,filename)  # here append filename with current filepath 
                CVconversion_pdf_to_txt.pdf_to_txt(newfilepath)    #call function for convert pdf2text
                # print(filename) 

# main()                
   

x=0
while(x==0):
    print("\n")
    print("WELCOME TO RESUME CONVERTION  (convert pdf/doc/docx format to textfile format)")
    print("****************************************************************************")
    x=int(input("Press 0 for continue..press 1 for exit..: "))
    if(x==1):
        print("---Exit---") 
        break  
    else:
        print("\n")
        print("-----------------FILE CONVERTION START------------------------")
        main()  
        os.chdir("../")
        print("-----------------FILE CONVERTION COMPLETED--------------------")
    

          
    


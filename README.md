# Development
A python app for converting pdf files to images. The script itself is made of different functions, each doing a specific task. so changing the functionality is easy if you want to add any features.

## Usage
The script is available both as a python script(script.py) and as an executable file(script.exe), which i used pyinstaller to make it. if you want to take a look at the code open the python file and if you want to just convert some pdf files run the executable file.

To use this script put all pdf files you want to convert in the "pdfs" directory. pdfs directory itself should be in the same directory that the script is in. then run the script. after execution, In images directory, for each pdf file, there will be a directory with the name of the pdf file which contains all images for that pdf file. 

Depending on the pdf files's size conversion may take some time!

## Requirements for the python script
You need to have python installed on your device. you also need to have [pdf2image] module (https://pypi.org/project/pdf2image/) installed and please pay attention to instructions for installing this module. As mentioned in the module's page, if you are on windows, you need to install poppler too.
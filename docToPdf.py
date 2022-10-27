from docx2pdf import convert
import glob, os
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filedir",help ="original file path")
parser.add_argument("--d", help="delete docx files", action='store_true')

args = parser.parse_args()
filedir = args.filedir

p = Path(filedir)
FileList=list(p.glob("**/*.docx")) 
print(FileList)

for file in FileList:
    filename = str(file).split(".")[0]
    # print(filename)
    convert(file,f"{filename}.pdf")

if args.d == True:
    for file in FileList:
        os.remove(file)
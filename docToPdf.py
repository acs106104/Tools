from docx2pdf import convert
import glob
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filedir",help ="original file path")

args = parser.parse_args()
filedir = args.filedir

p = Path(filedir)
FileList=list(p.glob("**/*.docx")) 
print(FileList)

for file in FileList:
    filename = str(file).split(".")[0]
    # print(filename)
    convert(file,f"{filename}.pdf")

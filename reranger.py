import os
from bs4 import BeautifulSoup
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("original_filedir",help ="original file path")
parser.add_argument("target_filedir",help ="target file path")

args = parser.parse_args()
filedir = args.original_filedir
newfiledir = args.target_filedir

if not os.path.exists(newfiledir):
    os.makedirs(newfiledir)

for filename in os.listdir(filedir):
    # print(filename)
    temp = filename.split("_")
    # print(temp)
    name = temp[0]
    # print(name)

    if len(temp) < 3:
        continue
    nowfiledir = os.path.join(filedir, filename)
    if temp[3] == 'onlinetext':
        for cfilename in os.listdir(nowfiledir):
            nowcfiledir = os.path.join(filedir, filename, cfilename)
            # 读取html内容
            html_content = open(nowcfiledir, 'rb')
            text = BeautifulSoup(html_content, "html.parser").get_text()

            if text.strip() != '':
                # 去除 .html
                text_name = cfilename[: -5]

                with open(f"{newfiledir}/{name}.txt".format(cfilename), "a", encoding="utf-8") as file_handle:
                    file_handle.write(text)
                    file_handle.write('\n')  
        # print('onlinetext')
    else:
        i = 0
        if len(os.listdir(nowfiledir)) > 1:
            i+=1
        for cfilename in os.listdir(nowfiledir):
            # print(i)
            index = '' if i==0 else i
            # print(os.path.join(newfiledir, cfilename))
            newfilename = name + str(index) + "." + cfilename.split(".")[-1]
            print(newfilename)
            shutil.copyfile(os.path.join(filedir, filename, cfilename), os.path.join(newfiledir, newfilename))
            i =i + 1
        # print('hw')

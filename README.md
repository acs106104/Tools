# Tools
#### 不定時開發簡單的小工具...

> 之後 maybe 會將這兩個檔案整合：）讓助教改作業可以方便點！

## reranger.py
從 [ecourse2](ecourse2.ccu.edu.tw "ecourse2") 上面下載的作業，可以將檔案整理至同一個文件夾。
檔案命名格式：學號+姓名
####Usage
```bash
python3 reranger.py [-h] original_filedir target_filedir
```
####Positional arguments
`original_filedir`  original file path
`target_filedir`    target file path

####Options:
`-h, --help`        show this help message and exit


##docToPdf.py
轉換資料夾中的所有的 .docx 檔至 .pdf 檔
#### Usage
```bash
python3 docTopdf.py [-h] [--d] filedir
```
#### Positional arguments
  `filedir` original file path


#### Options
`  -h, --help`  show this help message and exit
 ` --d `        delete docx files

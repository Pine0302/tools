import os
import shutil

'''
获取doc文件名，创建docx文件路径
'''
filesList = []

# 源文件路径
sourcePath = "/home/pine/html/pdf"
# 目标文件路进
destPath = "/home/pine/html/tt"

def handleFile(sourcePath):
    for root, dirs, files in os.walk(sourcePath):
        for file in files:
            if file.find(".") != -1:
                suffix = file.split('.')[1]
                if suffix == 'pdf':
                    # 去掉文件名的空格
                    if file.find(" ") != -1:
                        oldfile = file
                        file = file.replace(" ", "-")
                        shutil.copy(sourcePath + "/" + oldfile, sourcePath + "/" + file)
                        os.remove(sourcePath + "/" + oldfile)
                    filesList.append(file)
                    os.system("libreoffice --headless  --infilter='writer_pdf_import' --convert-to doc %s --outdir %s" % (sourcePath + "/" +file, destPath))
        for dir in dirs:
            handleFile(sourcePath + "/" + dir)
        return filesList


#import_file_name = "/test/seo.docx"
#output_file_path = "/test/"
#os.system("libreoffice --headless  --infilter='writer_pdf_import' --convert-to doc %s --outdir %s" % (import_file_name, output_file_path))

try:
    fileNameList = handleFile(sourcePath)
    #print(fileNameList)
# docToDocx(fileNameList)
finally:
    exit
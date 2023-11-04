import os
import shutil

'''
获取doc文件名，创建docx文件路径
'''
filesList = []

# 源文件路径
sourcePath = "/home/pine/workspace/model/tempFile/newdoc1"
# 目标文件路进
destPath = "/home/pine/workspace/model/tempFile/docx1"

def handleFile(sourcePath):
    for root, dirs, files in os.walk(sourcePath):
        for file in files:
            if file.rfind(".doc") != -1:
                suffix = file.split('.do')[1]
                if suffix == 'c':
                    # 去掉文件名的空格
                    if file.find(" ") != -1:
                        oldfile = file
                        file = file.replace(" ", "-")
                        shutil.copy(sourcePath + "/" + oldfile, sourcePath + "/" + file)
                        os.remove(sourcePath + "/" + oldfile)
                    filesList.append(file)
                    os.system("libreoffice --headless --convert-to docx %s --outdir %s" % (sourcePath + "/" +file, destPath))
                if suffix == 'cx':
                    shutil.copy(sourcePath + "/" + file, destPath + "/" + file)
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
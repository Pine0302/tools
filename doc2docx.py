import os
from win32com import client as wc

word = wc.Dispatch('Word.Application')
# 将docx文件保存的路径
docxPath = "C:\\Users\\pine-apple\\PycharmProjects\\doc2docx\\docx"
# doc文件路径
path = "C:\\Users\\pine-apple\\PycharmProjects\\doc2docx\\doc"

'''
获取doc文件名，创建docx文件路径
'''
filesList = []


def handleFile(path):
    for root, dirs, files in os.walk(path):
        isExists = os.path.exists(docxPath)
        # 新建docx文件夹
        if not isExists:
            os.makedirs(docxPath)
        for file in files:
            # 判断尾缀是不是doc
            suffix = file.split('.')[1]
            if suffix == 'doc':
                filesList.append(file)
                docToDocxSingle(path, file)
        for dir in dirs:
            handleFile(path + "\\" + dir)
        return filesList


'''
将doc文件转换成docx文件
'''


def docToDocxSingle(path, fileName):
    try:
        print("开始处理     文件名：" + fileName)
        doc = word.Documents.Open(path + '\\' + fileName)
        # [:-4]的意思是选这个字符串从开始到最后倒数第4位（不含）
        docxNamePath = docxPath + '\\' + fileName[:-4] + '.docx'
        print('转换完成！' + docxNamePath)
        doc.SaveAs(docxNamePath, 12, False, "", True, "", False, False, False, False)

    finally:
        # 一定要记得关闭docx，否则会出现文件占用
        doc.Close()


def docToDocx(fileNameList):
    try:
        for fileName in fileNameList:
            print("开始处理     文件名：" + fileName)
            doc = word.Documents.Open(path + '\\' + fileName)
            # [:-4]的意思是选这个字符串从开始到最后倒数第4位（不含）
            docxNamePath = docxPath + '\\' + fileName[:-4] + '.docx'
            print('转换完成！' + docxNamePath)
            doc.SaveAs(docxNamePath, 12, False, "", True, "", False, False, False, False)

    finally:
        # 一定要记得关闭docx，否则会出现文件占用
        doc.Close()


try:
    fileNameList = handleFile(path)
    print(fileNameList)
# docToDocx(fileNameList)
finally:
    word.Quit()

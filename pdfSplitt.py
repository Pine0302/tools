import sys
from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_path, output_path, start_page, end_page):
    with open(input_path, 'rb') as input_file:
        pdf = PdfReader(input_file)
        total_pages = len(pdf.pages)

        # 处理起始页和结束页超出范围的情况
        if start_page < 0:
            start_page = 0
        if end_page >= total_pages:
            end_page = total_pages - 1

        # 创建一个新的 PDF writer 对象，并拷贝指定页范围的页面
        output_pdf = PdfWriter()
        for page_num in range(start_page, end_page + 1):
            output_pdf.add_page(pdf.pages[page_num])

        # 将切割后的 PDF 页面保存到输出文件
        with open(output_path, 'wb') as output_file:
            output_pdf.write(output_file)


# 通过命令行参数获取传递的参数
# inputPath = sys.argv[1]
# outputPath = sys.argv[2]
# startPage = int(sys.argv[3])
# endPage = int(sys.argv[4])
inputPath = "/home/pine/Desktop/temp/01.pdf"
outputPath = '/home/pine/Desktop/temp/02.pdf'
startPage = 20
endPage = 35
a = startPage
while a<endPage:
    outputPath = '/home/pine/Desktop/temp/'+ str(a) +'.pdf'
    split_pdf(inputPath, outputPath, a, a+4)
    a = a+5

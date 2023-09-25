import PyPDF2

pdfFilePath = '/home/pine/html/pdf/Python基础视频课课件/ppt和pdf课件/1-python基础知识.pdf';

pdfFileObj = open(pdfFilePath, 'rb')

pdfReader = PyPDF2.PdfReader(pdfFileObj)

for page in pdfReader.pages:

    print(page.extractText())
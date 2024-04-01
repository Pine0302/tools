#import os
import time
#import pytesseract
#import pyperclip
import logging
import xerox

#from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#from image_processer import process_image_self,preprocess_image
from alioss import upload2oss
from baiduocr import ocr

#logging.basicConfig(filename='/home/pine/workspace/pythontool/test.txt', level=logging.INFO)

#基于监控截屏文件夹的文件变动来找到截屏图片并解析成文字的方案
class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        # 当文件被创建时调用
        if not event.is_directory:
            #print(f'新截屏被检测到: {event.src_path}')
            #logging.info(f'新截屏被检测到: {event.src_path}')
            file_url = upload2oss(event.src_path)
            logging.info(f'file_url: {file_url}')
            #使用百度ocr识别
            #words = ocr(file_url)
            words = ocr(event.src_path)
            #logging.info(f'words: {words}')
            #print(text_to_copy)
            #pyperclip.copy(words)
            xerox.copy(words)
            #使用pytesseract做ocr识别
            #process_image_self(preprocess_image(event.src_path))

# 替换为你的截屏保存路径
screenshots_folder = '/home/pine/Pictures/gnome-screenshot'

if __name__ == "__main__":
    #logging.info('This is an info message')
    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, path=screenshots_folder, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

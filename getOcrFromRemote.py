# -*- coding: utf-8 -*-
import time
import logging
import xerox
import requests
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alioss import upload2oss
from baiduocr import ocr,get_access_token

logging.basicConfig(filename='/home/pine/workspace/pythontool/test.log', level=logging.INFO)
#基于监控截屏文件夹的文件变动来找到截屏图片并解析成文字的方案
class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        # 当文件被创建时调用
        if not event.is_directory:
            #print(f'新截屏被检测到: {event.src_path}')
            logging.info(f'新截屏被检测到: {event.src_path}')
            time.sleep(1)
            # 指定远程服务器的 URL，在远程服务器上实现该功能
            SN_BAIDU_OCR_IP_PORT = os.getenv('SN_BAIDU_OCR_IP_PORT')  
            url = f'http://{SN_BAIDU_OCR_IP_PORT}/process_image' 
            with open(event.src_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(url, files=files)
        # 检查响应状态码是否为 200 OK
        if response.status_code == 200:
            # 提取处理后的结果
            result = response.json()['result']
            xerox.copy(result)
            return result
        else:
            logging.info('Error:', response.status_code)
            return None
# 替换为你的截屏保存路径
screenshots_folder = '/home/pine/Pictures/gnome-screenshot'

if __name__ == "__main__":
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

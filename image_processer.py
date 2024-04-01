# image_processor.py
import pytesseract
from PIL import Image,ImageEnhance,ImageFilter
import pyperclip

#图像预处理
def preprocess_image(image_path):
    image = Image.open(image_path)
    # 增加对比度
    enhancer = ImageEnhance.Contrast(image)
    image_enhanced = enhancer.enhance(2)
    # 应用轻微的模糊过滤器，有时可以帮助提高OCR的准确性
    image_blurred = image_enhanced.filter(ImageFilter.SMOOTH)
    return image_blurred

#    """处理图像文件，并将识别的文本复制到剪贴板"""
def process_image(image_path):
    """处理图像文件，并将识别的文本复制到剪贴板"""
    text = pytesseract.image_to_string(Image.open(image_path), lang='chi_sim+eng')
    pyperclip.copy(text)
    print(f'截屏文字内容: {text}')

def process_image_self(image):
    """处理图像文件，并将识别的文本复制到剪贴板"""
    text = pytesseract.image_to_string(image, lang='chi_sim+eng')
    pyperclip.copy(text)
    print(f'截屏文字内容: {text}')
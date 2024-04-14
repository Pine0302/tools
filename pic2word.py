from flask import Flask, request, jsonify
from baiduocr import ocr,get_access_token
from werkzeug.utils import secure_filename
import logging
app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file_storage = request.files['file']
    
    # 检查文件名是否以 .png 结尾
    if not file_storage.filename.endswith('.png'):
        return jsonify({'error': 'File must be a PNG image'})
    
    temp_filename = '/root/pine/pythontool/temp/' + secure_filename(file_storage.filename)
    file_storage.save(temp_filename)
    logging.info(f"temp_file_name"+temp_filename)
    words = ocr(temp_filename)

    return jsonify({'result': words})
    # 读取文件内容
   # image_data = file.read()

    # 对图像数据进行处理，这里简单地将其转换为 Base64 编码的字符串
    #encoded_image = base64.b64encode(image_data).decode('utf-8')

    # 返回处理后的字符串
    #return jsonify({'result': encoded_image})

if __name__ == '__main__':
      # 设置 host 参数为 '0.0.0.0'，端口为 80（假设你想监听 80 端口）
    app.run(host='0.0.0.0', port=3020,debug=True)

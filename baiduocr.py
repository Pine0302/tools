import base64
import urllib
import requests
import os
import json
import logging
logging.basicConfig(filename='/home/pine/workspace/pythontool/test.log', level=logging.INFO)
def ocr(image_path):
    access_token = os.getenv('BAIDU_ACCESS_TOKEN')   
    if access_token is None:
        print("Access TOKEN is None. Check your environment variables.")
        exit(1) 
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + access_token #高精度
    image = get_file_content_as_base64(image_path,True)
    payload='image='+image+'&detect_direction=false&paragraph=false&probability=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    logging.info(f'data: {data}')
    words_results = [item["words"] for item in data["words_result"]]
    text_to_copy = '\n'.join(words_results)
    return text_to_copy
    

def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded 
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    access_key_id = os.getenv('BAIDU_ACCESS_KEY_ID')
    access_key_secret = os.getenv('BAIDU_ACCESS_KEY_SECRET')
    if access_key_id is None or access_key_secret is None:
        print("Access key ID or secret is None. Check your environment variables.")
        # 可以在这里添加逻辑来处理这个错误，比如退出程序
        exit(1)


    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": access_key_id, "client_secret": access_key_secret}
    response = requests.post(url, params=params).json()
    print(str(response))
    return str(response.get("access_token"))

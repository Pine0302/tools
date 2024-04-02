import os
import oss2
import re
import logging
logging.basicConfig(filename='/home/pine/workspace/pythontool/test.log', level=logging.INFO)

def upload2oss(image_path):
    #logging.info(f'upload2oss: {image_path}')
    # 从环境变量获取 AccessKeyId 和 AccessKeySecret
    access_key_id = os.getenv('ALIYUN_ACCESS_KEY_ID')
    #logging.info(f'access_key_id: {access_key_id}')
    access_key_secret = os.getenv('ALIYUN_ACCESS_KEY_SECRET')
    if access_key_id is None or access_key_secret is None:
        logging.info("Access key ID or secret is None. Check your environment variables.")
        # 可以在这里添加逻辑来处理这个错误，比如退出程序
        exit(1)

    # 配置 Endpoint 和 Bucket 名称
    endpoint = 'oss-cn-hangzhou.aliyuncs.com'  # 修改为你的实际Endpoint
    bucket_name = 'pine-static'  # 你的Bucket名称

    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, f'https://{endpoint}', bucket_name)

    # 从本地文件路径提取文件名作为OSS中的Key
    filename = os.path.basename(image_path)
    print(f"文件名： {filename} ")
    # 使用字符串方法和格式化来转换文件名
    key = re.sub(r"屏幕截图", "", filename)
    key = re.sub(r" ", "-", key)

    # 上传文件
    bucket.put_object_from_file(key, image_path)
    #print(f"文件 {image_path} 已上传至 OSS。")

    # 构建文件访问链接
    file_url = f"http://{bucket_name}.{endpoint}/{key}"
    #print(f"文件访问链接：{file_url}")

    return file_url

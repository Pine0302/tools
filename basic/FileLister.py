import os

class FileLister:
    def __init__(self, directory):
        self.directory = directory
    
    def list_files(self):
        # 检查目录是否存在
        if not os.path.exists(self.directory):
            print("目录不存在")
            return []
        
        # 检查是否是一个目录
        if not os.path.isdir(self.directory):
            print("指定的路径不是一个目录")
            return []
        
        # 获取目录中的所有文件
        files = []
        for root, dirs, filenames in os.walk(self.directory):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                files.append(file_path)
        
        return files

import chardet

class FileReader:
    def __init__(self, filename, encoding='utf-8'):
        self.filename = filename
        self.encoding = self.detect_encoding()

    def detect_encoding(self):
        try:
            with open(self.filename, 'rb') as f:
                result = chardet.detect(f.read())
                encoding = result['encoding']
                return encoding
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except UnicodeDecodeError:
            print(f"Error: Unable to decode the file '{self.filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def read(self):
        try:
            with open(self.filename, 'r', encoding=self.encoding) as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
            return
        except UnicodeDecodeError:
            print(f"Error: Unable to decode the file '{self.filename}' with encoding '{self.encoding}'.")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return

    def read_lines(self, num_lines=None):
        try:
            with open(self.filename, 'r', encoding=self.encoding) as file:
                if num_lines:
                    lines = islice(file, num_lines)
                else:
                    lines = file.readlines()
                return lines
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except UnicodeDecodeError:
            print(f"Error: Unable to decode the file '{self.filename}' with encoding '{self.encoding}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

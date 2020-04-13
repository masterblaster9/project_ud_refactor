import base64
import os


def encode_file(file_path):

    with open(file_path, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('ascii')
        return base64_message


PATH = "/Users/{}/.aws/credentials".format(os.getenv("USER"))

if __name__ == '__main__':
    file_path = PATH
    print(encode_file(file_path))

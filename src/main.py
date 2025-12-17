
import json

if __name__ == '__main__':
    file_path = '../logs/zoom_access_token.json'

    with open(file_path,'r') as file:
        data = json.load(file)


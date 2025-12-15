#synchronous zoom api calls

import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url).json()

    for key, values in response.items():
        print(f'{key} : {values}')
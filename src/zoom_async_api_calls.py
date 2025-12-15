#asynchronous Zoom api calls with batch runner functions

import httpx
import asyncio


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/posts/1'

    with httpx.Client() as client:
        response = client.get(url).json()

    for key, values in response.items():
        print(f'{key} : {values}')
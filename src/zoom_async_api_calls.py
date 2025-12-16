#asynchronous Zoom api calls with batch runner functions

import httpx
import asyncio

async def fetch(url:str, client: httpx.AsyncClient):

    response = await client.get(url)
    return response


async def fetch_batch_urls(urls: list[str]):

    async with httpx.AsyncClient() as client:
        task = [asyncio.create_task(fetch(url,client)) for url in urls]
        response = await asyncio.gather(*task)

    return response




def main():

    url = 'https://webhook.site/73f56245-f9a2-4e33-b5b7-73b9f998cf58'
    urls = [url for _ in range(0,10)]

    responses = asyncio.run(fetch_batch_urls(urls))

    for each_response in responses:
        print(each_response)

    # url = 'https://jsonplaceholder.typicode.com/posts/1'
    #
    # with httpx.Client() as client:
    #     response = client.get(url).json()
    #
    # for key, values in response.items():
    #     print(f'{key} : {values}')



if __name__ == '__main__':
    main()